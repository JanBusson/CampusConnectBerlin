from flask import render_template, abort, redirect, url_for
from . import main_bp
from dao.user_dao import user_dao
from forms.form_welcome import CreateWelcomeForm

@main_bp.route('/welcome/<int:user_id>', methods=['GET', 'POST'])
def welcome(user_id):
    form=CreateWelcomeForm()
    user = user_dao.get_uid(user_id)
    #Welcome Seite mit entsprechendem User
    if user:
        
        #Reaktion auf User Input
        if form.validate_on_submit():
          if form.find_matches.data:
            return redirect(url_for('main.matching',user_id=user.user_id))
#        elif form.set_filters.data:
#            return redirect(url_for('main.register'))
#        elif form.my_matches.data:
#            return redirect(url_for('main.register'))
        
        return render_template('welcome.html',form=form,user=user)
    else:
        abort(404)


     