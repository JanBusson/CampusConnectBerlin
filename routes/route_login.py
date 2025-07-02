from flask import render_template,redirect, url_for, flash, session
from . import main_bp
from forms.form_login import CreateLoginForm
from dao.user_dao import user_dao

@main_bp.route('/login', methods=['GET', 'POST']) 
def login():
    form = CreateLoginForm()

    if form.validate_on_submit():
        #Auslesen der Eingaben
        email = form.email.data
        password = form.password.data
        
        #gibt entweder den User mit den entsprechenden Login Daten zurück bei korrekter Eingabe oder none
        user = user_dao.check_user_credentials(email,password)

        if user:
            session['user_id']=user.user_id
            return redirect(url_for('main.welcome'))
        else:
            flash('Login fehlgeschlagen. Bitte überprüfe Benutzername und Passwort.')
            return redirect(url_for('main.login'))

    
    return render_template('login.html', form=form)