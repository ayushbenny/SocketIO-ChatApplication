from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a chat room.

    Validates user input and creates a session. If form input is invalid, displays error messages on page.
    
    Returns:
        A HTTP redirect response to the chat page.
        
    Raises:
        None
        
    """
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """
    Presents the chat room page. 

    Users must provide their name and room, which are stored in the session to maintain their identity.
    If the user's name or room are not present in the session, the function redirects them to index page.

    Returns:
        str: HTML template for chat room page with user's name and room as arguments
    """
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
