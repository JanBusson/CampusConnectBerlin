from flask import render_template,redirect, url_for, flash, session
from . import main_bp
from dao.match_dao import match_dao
from dao.user_dao import user_dao

@main_bp.route('/evaluate_match', methods=['GET', 'POST']) 
def chat():
    user_id= session.get('user_id')
    currUser = user_dao.get_uid(user_id)
    matches = match_dao.get_all_for_uid(user_id=user_id)
    
    return render_template('chat.html',matches=matches,currUser=currUser)