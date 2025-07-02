#zeigt ein User Profil
from . import main_bp
from flask import render_template, session
from dao.user_dao import user_dao
from dao.match_dao import match_dao
from dao.personality_dao import personality_dao
from services.user_service import calculate_age
from forms.form_matching import CreateMatchingForm

@main_bp.route('/matching', methods=['GET', 'POST']) 
def matching():
     curr_user_id = session.get('user_id')
     user= match_dao.get_random_user(curr_user_id)
     age = calculate_age(user.birth_date)
     personality_sore = personality_dao.get_type_by_uid(user.user_id)
     form=CreateMatchingForm()
     if form.validate_on_submit():
          return
     return render_template('matching.html', user=user,age=age,personality_sore=personality_sore,form=form)
