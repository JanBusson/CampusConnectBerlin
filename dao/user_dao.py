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
    def create_user(cls, name, email, password, age, uni_id):
        new_user = User(
            name=name,
            email=email,
            password=password,
            age=age,
            uni_id=uni_id
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
