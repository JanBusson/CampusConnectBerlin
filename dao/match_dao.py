from models import Match, Swipe, User
from db import db
from datetime import date
from services.match_service import MatchService

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

    @classmethod
    def is_mutual_like(cls, user1_id, user2_id):
        like1 = Swipe.query.filter_by(swiper_id=user1_id, swiped_id=user2_id, swipe_type='like').first()
        like2 = Swipe.query.filter_by(swiper_id=user2_id, swiped_id=user1_id, swipe_type='like').first()
        return like1 and like2

    @classmethod
    def create_if_mutual_like(cls, user1_id, user2_id):
        if not cls.is_mutual_like(user1_id, user2_id):
            return None

        existing = Match.query.filter(
            ((Match.user1_id == user1_id) & (Match.user2_id == user2_id)) |
            ((Match.user1_id == user2_id) & (Match.user2_id == user1_id))
        ).first()
        if existing:
            return existing

        user1 = User.query.get(user1_id)
        user2 = User.query.get(user2_id)
        result1 = user1.personality_result if user1 else None
        result2 = user2.personality_result if user2 else None

        if not result1 or not result2:
            return None

        # Kompatibilität berechnen via match_service
        score = MatchService.calculate_compatibility(result1, result2)

        return cls.create_match(user1_id, user2_id, score, "pending", date.today())