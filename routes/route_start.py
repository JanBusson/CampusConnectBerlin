from flask import render_template,redirect, url_for
from . import main_bp
from forms.form_start import CreateStartForm

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = CreateStartForm()
    if form.validate_on_submit():
        if form.login.data:
            return redirect(url_for('main_bp.login'))
        elif form.register.data:
            return redirect(url_for('main_bp.register'))
    return render_template('start.html', form=form)
