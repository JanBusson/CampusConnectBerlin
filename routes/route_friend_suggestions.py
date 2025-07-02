from flask import render_template, session
from . import main_bp
from dao.match_dao import match_dao


@main_bp.route('/friend_suggestions')
def friend_suggestions():
    form=CreateWelcomeForm()
    user_id = session.get('user_id')
    match_dao.get_all_for_uid(user_id=user_id)
    return render_template('friend_suggestions.html')