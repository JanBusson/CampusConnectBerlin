from flask import render_template, abort, redirect, url_for, session
from . import main_bp
from dao.user_dao import user_dao
from forms.form_welcome import CreateWelcomeForm

@main_bp.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form=CreateWelcomeForm()
    user_id = session.get('user_id')
    user = user_dao.get_uid(user_id)
    #Welcome Seite mit entsprechendem User
    if user:
        
        #Reaktion auf User Input
        if form.validate_on_submit():
            if form.find_matches.data:
                return redirect(url_for('main.matching',user_id=user.user_id))
            elif form.my_matches.data:
                return redirect(url_for('main.my_matches'))
            #elif form.friend_suggestions.data:
            #   return redirect(url_for('main.friend_suggestions'))
            elif form.my_chats:
                return redirect(url_for('main.chat'))
        
        return render_template('welcome.html',form=form,user=user)
    else:
        abort(404)


     