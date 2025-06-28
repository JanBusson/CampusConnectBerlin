from models import Match
from db import db

class match_dao:
    @classmethod
    def get_all_for_uid(cls, user_id):
        return Match.query.filter(
            (Match.user1_id == user_id) | (Match.user2_id == user_id)
        ).all()

    @classmethod
    def create_match(cls, user1_id, user2_id, compatibility, status, matched_at):
        match = Match(
            user1_id=user1_id,
            user2_id=user2_id,
            compatibility=compatibility,
            status=status,
            matched_at=matched_at
        )
        db.session.add(match)
        db.session.commit()
        return match
