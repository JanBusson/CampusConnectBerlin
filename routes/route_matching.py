#zeigt ein User Profil
from . import main_bp
from flask import render_template
from dao.user_dao import user_dao
from services.user_service import calculate_age

@main_bp.route('/matching/<int:user_id>', methods=['GET', 'POST']) 
def matching(user_id):
     user= user_dao.get_uid(user_id=user_id)
     age = calculate_age(user.birth_date)
     return render_template('matching.html', user=user,age=age)
