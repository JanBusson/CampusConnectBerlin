from app import app
from dao.match_dao import match_dao
from models import Match
from datetime import datetime, timedelta

with app.app_context():
    matches = Match.query.all()

    # Beispielhafter längerer Dialog (4 Messages pro User)
    conversation = [
        ("Hey, nice to meet you here!", "Hey! Same here 😊 How are you liking the app so far?"),
        ("Honestly pretty cool so far. The design is nice!", "Yeah, and people seem friendly."),
        ("Are you from Berlin originally?", "Nope, I moved here for uni. You?"),
        ("Same! Still figuring out the best cafés around.", "Let's compare notes sometime!")
    ]

    for i, match in enumerate(matches):
        # Nur bei ca. ⅔ der Matches einen Verlauf anlegen
        if i % 3 == 0:
            continue

        try:
            base_time = datetime.now() - timedelta(days=i)
            for j, (msg1, msg2) in enumerate(conversation):
                # Abwechselnd schreiben
                msg_time = base_time + timedelta(minutes=j * 4)
                match_dao.save_message(match.match_id, match.user1_id, msg1)
                match_dao.save_message(match.match_id, match.user2_id, msg2)
            print(f"💬 Vollständiger Chatverlauf für Match {match.match_id} gespeichert.")
        except Exception as e:
            print(f"⚠️ Fehler beim Speichern für Match {match.match_id}: {e}")

    print("✅ Ausführliche Beispiel-Chats wurden gespeichert.")
