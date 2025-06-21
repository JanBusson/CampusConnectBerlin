# testDB.py
from app import app                    # deine Flask-App wird importiert
from dao.university_dao import university_dao  # DAO für Uni-Datenbank
# Application Context starten
with app.app_context():
    university_dao.create_university(
        name="Humboldt-Universität zu Berlin",
        short_name="HU Berlin",
        location="Berlin"
    )
    print("Uni erfolgreich eingefügt.")
