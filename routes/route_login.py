from flask import Blueprint, render_template,redirect, url_for
from . import main_bp
from forms.form_login import CreateLoginForm

@main_bp.route('/login', methods=['GET', 'POST']) 
def login():
    form = CreateLoginForm()

    if form.validate_on_submit():
        # TODO Login prüfen
        return redirect(url_for('main_bp.welcome'))
    
    return render_template('login.html', form=form)