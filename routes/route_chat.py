from flask import render_template,redirect, url_for, flash, session
from . import main_bp
from forms.form_login import CreateLoginForm
from dao.match_dao import match_dao
from dao.user_dao import user_dao
from models import Match

@main_bp.route('/chat', methods=['GET', 'POST']) 
def matching():
    user_id= session.get('user_id')
    currUser = user_dao.get_uid(user_id)
    matches = match_dao.get_all_for_uid(user_id=user_id)
    
    return render_template('my_matches.html',matches=matches,currUser=currUser)