from flask import render_template, abort
from . import main_bp
from dao.university_dao import university_dao
from dao.user_dao import user_dao
from forms.form_register import CreateRegisternForm
import bcrypt

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form=CreateRegisternForm()
    form.university.choices = [(u.uni_id, u.name) for u in university_dao.get_all()]

    if form.validate_on_submit():
    # Auslesen der Eingaben
        name = form.name.data
        email = form.email.data
        university_id = form.university.data
        birthday = form.birthday.data
        password = form.password.data
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_dao.create_user(name=name,email=email,password=hashed_pw,uni_id=university_id,age=birthday)

    return render_template('register.html', form=form)