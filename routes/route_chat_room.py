from flask import render_template,redirect, url_for, flash, session
from . import main_bp
from dao.match_dao import match_dao
from dao.user_dao import user_dao
from forms.form_chat_room import CreateChatForm


@main_bp.route('/chat/<int:match_id>', methods=['GET', 'POST']) 
def chat_room(match_id):
    user_id = session.get('user_id')
    curr_user = user_dao.get_uid(user_id)
    match = match_dao.get_by_id(match_id)
    form =CreateChatForm()

    #Speichern des anderen Nutzers
    other_user = match.user2 if match.user1.user_id == user_id else match.user1
    #Nachrichten als Liste => in das Template laden
    messages = match_dao.get_messages_for_match(match_id)
    if form.validate_on_submit():
       content = form.message.data.strip()
       if content:
           match_dao.save_message(match_id, user_id, content)
       return redirect(url_for('main.chat_room', match_id=match_id))
    
    return render_template('chat_room.html',form=form,curr_user=curr_user, other_user=other_user, messages=messages, match_id=match_id)