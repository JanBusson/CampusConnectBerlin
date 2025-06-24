#zeigt ein User Profil
from . import main_bp
from flask import render_template
from dao.user_dao import user_dao

@main_bp.route('/matching/<int:user_id>', methods=['GET', 'POST']) 
def matching(user_id):
     user= user_dao.get_uid(user_id=user_id)


     return render_template('matching.html', user=user)
