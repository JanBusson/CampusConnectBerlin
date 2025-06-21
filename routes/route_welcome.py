from flask import render_template, abort
from . import main_bp
from dao.user_dao import user_dao
from forms.form_welcome import CreateStartForm

@main_bp.route('/welcome/<int:user_id>', methods=['GET'])
def welcome(user_id):
    user = user_dao.get_uid(user_id)
    #Welcome Seite mit entsprechendem User
    if user:
        return render_template('welcome.html', username=user.name)
    else:
        abort(404)