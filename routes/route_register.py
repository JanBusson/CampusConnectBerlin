from flask import render_template, abort
from . import main_bp
from dao.university_dao import university_dao
from forms.form_register import CreateRegisternForm

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form=CreateRegisternForm()
    form.university.choices = [(u.id, u.name) for u in university_dao.get_all()]
    
    return render_template('register.html', form=form)