#zeigt ein User Profil
from . import main_bp
from flask import render_template, session, redirect, url_for
from dao.match_dao import match_dao
from dao.swipe_dao import swipe_dao
from dao.personality_dao import personality_dao
from services.user_service import calculate_age
from services.swipe_service import SwipeService
from forms.form_matching import CreateMatchingForm

@main_bp.route('/matching', methods=['GET', 'POST']) 
def matching():
     curr_user_id = session.get('user_id')
     user= match_dao.get_random_user(curr_user_id)
     if user is None:
          return render_template('all_users_swiped.html')
     age = calculate_age(user.birth_date)
     personality_sore = personality_dao.get_type_by_uid(user.user_id)
     form=CreateMatchingForm()

     if form.validate_on_submit():
          if form.yes.data:
               #Nutzer A swipet (z. B. „like“ auf B)
               SwipeService.process_swipe(swiper_id= curr_user_id,swiped_id=user.user_id,swipe_type='like')
               return redirect(url_for('main.matching',user_id=curr_user_id))
          elif form.no.data:
               swipe_dao.create_swipe(swiper_id= curr_user_id,swiped_id=user.user_id,swipe_type='dislike')
               return redirect(url_for('main.matching',user_id=curr_user_id))
          elif form.back.data:
               return redirect(url_for('main.welcome'))
     return render_template('matching.html', user=user,age=age,personality_sore=personality_sore,form=form)
