from flask import send_file, abort
import io
from dao.user_dao import user_dao
from . import main_bp

@main_bp.route('/profile_picture{<int:user_id>')
def profile_picture(user_id):
    user = user_dao.get_uid(user_id)
    return send_file(io.BytesIO(user.profile_picture), mimetype='image/png')