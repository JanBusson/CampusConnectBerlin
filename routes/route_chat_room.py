from flask import render_template,redirect, url_for, flash, session
from . import main_bp
from forms.form_login import CreateLoginForm
from dao.match_dao import match_dao
from dao.user_dao import user_dao
from models import Match

@main_bp.route('/chat/<int:match_id>', methods=['GET', 'POST']) 
def chat_room(match_id):
    user_id = session.get('user_id')
    curr_user = user_dao.get_uid(user_id)
    match = match_dao.get_by_id(match_id)

    #Speichern des anderen Nutzers
    other_user = match.user2 if match.user1.user_id == user_id else match.user1
    #Nachrichten als Liste => in das Template laden
    messages = match_dao.get_messages_for_match(match_id)
    
    return render_template('chat_room.html',curr_user=curr_user, other_user=other_user, messages=messages, match_id=match_id)