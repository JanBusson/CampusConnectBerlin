from flask import render_template,redirect, url_for, session
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
        #TODO email unique checken
        email = form.email.data
        university_id = form.university.data
        birthday = form.birthday.data
        password = form.password.data
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        profile_picture_data=form.profilePic.data
        profile_picture= profile_picture_data.read()
        description = form.description.data

        #den neune Nutzer mit den Eingaben anlegen
        new_user = user_dao.create_user(name=name,email=email,password=hashed_pw,uni_id=university_id,birth_date=birthday,profile_picture=profile_picture,description=description)
        session['user_id']=new_user.user_id
        return redirect(url_for('main.quiz'))

    return render_template('register.html', form=form)