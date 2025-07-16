from db import db
from datetime import date
from models import Swipe, Match
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

    # (nachdem alle Matches erstellt wurden…)

    print("✔️ Alle Swipes verarbeitet.")

    # Matches laden, z. B. die ersten 10 zur Bewertung auswählen
    matches = Match.query.all()

    for i, match in enumerate(matches):
        # Bewertung nur für z. B. 70 % der Matches
        if i % 4 == 0:
            continue  # diesen Match unbewertet lassen

        # Bewertung durch beide Nutzer (1–5 Sterne)
        try:
            match_dao.evaluate_match(match.user1_id, match.match_id, rating=(i % 5) + 1)
        except Exception as e:
            print(f"⚠️ Fehler bei Bewertung durch User {match.user1_id}: {e}")

        try:
            match_dao.evaluate_match(match.user2_id, match.match_id, rating=((i + 2) % 5) + 1)
        except Exception as e:
            print(f"⚠️ Fehler bei Bewertung durch User {match.user2_id}: {e}")

    print("📝 Einige Matches wurden erfolgreich bewertet.")
