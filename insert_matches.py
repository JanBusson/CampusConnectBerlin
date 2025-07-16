from db import db
from datetime import date
from models import Swipe
from dao.match_dao import match_dao
from app import app

# Gegenseitige Likes → führen zu Matches
match_pairs = [
    (1, 2),
    (1, 5),
    (2, 8),
    (3, 6),
    (4, 10),
    (5, 8),
    (6, 9),
    (7, 10),
    (3, 1),
    (9, 2),
    (6, 1),
    (7, 2),
    (8, 3),
    (9, 4),
    (10, 5)
]

with app.app_context():
    for user1, user2 in match_pairs:
        # 1. Swipes anlegen
        swipe1 = Swipe(swiper_id=user1, swiped_id=user2, swipe_type='like', swiped_at=date.today())
        swipe2 = Swipe(swiper_id=user2, swiped_id=user1, swipe_type='like', swiped_at=date.today())

        db.session.add(swipe1)
        db.session.add(swipe2)
        db.session.commit()  # <-- wichtig, damit sie in der Abfrage sichtbar sind!

        # 2. Jetzt Match erzeugen
        result = match_dao.create_if_mutual_like(user1, user2)

        if result:
            print(f"✅ Match created between {user1} and {user2} (Score: {result.compatibility})")
        else:
            print(f"⚠️ No match created between {user1} and {user2}")

    print("✔️ Alle Swipes verarbeitet.")
