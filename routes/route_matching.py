#zeigt ein User Profil
from . import main_bp
from flask import render_template, session
from dao.user_dao import user_dao
from dao.personality_dao import personality_dao
from services.user_service import calculate_age

@main_bp.route('/matching', methods=['GET', 'POST']) 
def matching():
     user_id = session.get('user_id')
     user= user_dao.get_uid(user_id=user_id)
     age = calculate_age(user.birth_date)
     personality_sore = personality_dao.get_type_by_uid(user_id)
     return render_template('matching.html', user=user,age=age,personality_sore=personality_sore)
