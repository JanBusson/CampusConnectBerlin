from db import db
from datetime import date

class University(db.Model):
    __tablename__ = 'university'
    uni_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    short_name = db.Column(db.Text)
    location = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    uni_id = db.Column(db.Integer, db.ForeignKey('university.uni_id'))
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.Date, default=date.today)
    profile_picture = db.Column(db.LargeBinary, nullable=False)

    university = db.relationship('University', backref='students', lazy=True)
    personality_result = db.relationship('PersonalityResult', uselist=False, backref='user')

class PersonalityResult(db.Model):
    __tablename__ = 'personality_result'
    result_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True)
    vec_ei = db.Column(db.Float)
    vec_sn = db.Column(db.Float)
    vec_tf = db.Column(db.Float)
    vec_jp = db.Column(db.Float)
    mbti_type = db.Column(db.Text)
    completed_at = db.Column(db.Date)

class Swipe(db.Model):
    __tablename__ = 'swipe'
    swipe_id = db.Column(db.Integer, primary_key=True)
    swiper_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    swiped_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    swipe_type = db.Column(db.Text)  # e.g., 'like' or 'dislike'
    swiped_at = db.Column(db.Date)
    profile_picture = db.Column(db.LargeBinary, nullable=False)

class Match(db.Model):
    __tablename__ = 'match'
    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    compatibility = db.Column(db.Float)
    status = db.Column(db.Text)  # e.g., 'pending', 'accepted'
    matched_at = db.Column(db.Date)
