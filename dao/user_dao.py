from models import User
from db import db
import bcrypt

class user_dao:

    # Get user by UID
    @classmethod
    def get_uid(cls, user_id):
        return db.session.get(User, user_id)

    # Get user by email
    @classmethod
    def get_email(cls, email):
        return User.query.filter_by(email=email).first()

    # Create a new user
    @classmethod
    def create_user(cls, name, email, password, birth_date, uni_id, profile_picture):
        new_user = User(
            name=name,
            email=email,
            password=password,
            birth_date=birth_date,
            uni_id=uni_id,
            profile_picture=profile_picture
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    # Delete user by UID
    @classmethod
    def delete_user(cls, user_id):
        user = db.session.get(User, user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    # Check login credentials
    @classmethod
    def check_user_credentials(cls, email: str, password: str) -> User:
        user = cls.get_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            return user
        return None

    # Get profile picture data by UID
    @classmethod
    def get_profile_picture_by_uid(cls, user_id) -> bytes | None:
        user = db.session.get(User, user_id)
        return user.profile_picture if user else None