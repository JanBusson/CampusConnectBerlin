from db import db
from models import University

class university_dao:
    @classmethod
    def get_all(cls):
        return University.query.all()

    @classmethod
    def get_by_id(cls, uni_id):
        return db.session.get(University, uni_id)

    @classmethod
    def get_by_name(cls, name):
        return University.query.filter_by(name=name).first()

    @classmethod
    def create_university(cls, name, short_name=None, location=None):
        university = University(
            name=name,
            short_name=short_name,
            location=location
        )
        db.session.add(university)
        db.session.commit()
        return university

    @classmethod
    def delete_university(cls, uni_id):
        uni = db.session.get(University, uni_id)
        if uni:
            db.session.delete(uni)
            db.session.commit()
            return True
        return False
