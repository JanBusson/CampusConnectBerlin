from models import Match, Swipe, User, Message
from db import db
from datetime import date
from services.match_service import MatchService
from sqlalchemy.sql.expression import func

class match_dao:

    @classmethod
    def get_random_user(cls, current_user_id):
    # Alle ids die vom Nutzer geswiped wurden
        swiped_ids = db.session.query(Swipe.swiped_id).filter(Swipe.swiper_id == current_user_id)

        # Zufälliger User, der noch nciht geswiped wurde
        return User.query.filter(User.user_id != current_user_id).filter(~User.user_id.in_(swiped_ids)) \
            .order_by(func.random()).first()
            # ~ bedeutet sowas wie NOT; \ dient zu Zeilenumbrüchen in Python

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
    
    #Nachricht auslesen zwischen Matches
    @classmethod
    def get_messages_for_match(cls, match_id):
        return Message.query.filter_by(match_id=match_id).order_by(Message.timestamp).all()

    #Nachrichten schreiben
    @classmethod
    def save_message(cls, match_id, sender_id, text):
        msg = Message(match_id=match_id, sender_id=sender_id, text=text)
        db.session.add(msg)
        db.session.commit()

    #wird gebraucht bei Nachrichten
    @classmethod
    def get_by_id(cls, match_id):
        return Match.query.get(match_id)
    
    #für die Bewertung der Matches
    @classmethod
    def evaluate_match(cls, user_id, match_id, rating):
        match = Match.query.get(match_id)
        if not match:
            raise ValueError("Match nicht gefunden.")

        if match.user1_id == user_id:
            if match.evaluated_by_user1:
                raise ValueError("Schon bewertet.")
            match.rating_by_user1 = int(rating)
            match.evaluated_by_user1 = True

        elif match.user2_id == user_id:
            if match.evaluated_by_user2:
                raise ValueError("Schon bewertet.")
            match.rating_by_user2 = int(rating)
            match.evaluated_by_user2 = True

        else:
            raise ValueError("User gehört nicht zum Match.")

        db.session.commit()