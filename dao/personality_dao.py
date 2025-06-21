from models import PersonalityResult
from db import db

class personality_dao:

    # Get personality result by UID
    @classmethod
    def get_by_uid(cls, user_id: int) -> PersonalityResult:
        return PersonalityResult.query.filter_by(user_id=user_id).first()

    # Create a new personality result
    @classmethod
    def create_result(cls, user_id, vec_ei, vec_sn, vec_tf, vec_jp, mbti_type, completed_at):
        result = PersonalityResult(
            user_id=user_id,
            vec_ei=vec_ei,
            vec_sn=vec_sn,
            vec_tf=vec_tf,
            vec_jp=vec_jp,
            mbti_type=mbti_type,
            completed_at=completed_at
        )
        db.session.add(result)
        db.session.commit()
        return result

    # Get only the MBTI type by UID
    @classmethod
    def get_type_by_uid(cls, user_id: int) -> str | None:
        result = cls.get_by_uid(user_id)
        return result.mbti_type if result else None
