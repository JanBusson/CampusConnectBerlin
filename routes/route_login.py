from flask import Blueprint, render_template
from . import main_bp
from forms.form_login import CreateLoginForm

login_bp = Blueprint('login', __name__) 

@main_bp.route('/login')
def login():
    form = CreateLoginForm()

    if form.validate_on_submit():
        # TODO Login prüfen
        return "Login erfolgreich!"  # Platzhalter
    
    return render_template('login.html', form=form)