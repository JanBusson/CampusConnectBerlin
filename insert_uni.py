import json
from db import db
from models import University
from app import app

# Berliner Hochschulen mit Geo-Koordinaten
berliner_hochschulen = [
    {"name": "Freie Universität Berlin", "short_name": "FU Berlin", "location": json.dumps({"lat": 52.4573, "lon": 13.2965})},
    {"name": "Humboldt-Universität zu Berlin", "short_name": "HU Berlin", "location": json.dumps({"lat": 52.5176, "lon": 13.3933})},
    {"name": "Technische Universität Berlin", "short_name": "TU Berlin", "location": json.dumps({"lat": 52.5125, "lon": 13.3266})},
    {"name": "Universität der Künste Berlin", "short_name": "UdK Berlin", "location": json.dumps({"lat": 52.5122, "lon": 13.3254})},
    {"name": "Alice Salomon Hochschule Berlin", "short_name": "ASH Berlin", "location": json.dumps({"lat": 52.5442, "lon": 13.6032})},
    {"name": "Berliner Hochschule für Technik", "short_name": "BHT", "location": json.dumps({"lat": 52.5456, "lon": 13.3497})},
    {"name": "HTW Berlin", "short_name": "HTW Berlin", "location": json.dumps({"lat": 52.4930, "lon": 13.5262})},
    {"name": "HWR Berlin", "short_name": "HWR Berlin", "location": json.dumps({"lat": 52.4666, "lon": 13.3517})},
    {"name": "Evangelische Hochschule Berlin", "short_name": "EHB", "location": json.dumps({"lat": 52.4333, "lon": 13.2556})},
    {"name": "Hertie School", "short_name": "Hertie", "location": json.dumps({"lat": 52.5211, "lon": 13.3806})},
    {"name": "ESCP Business School", "short_name": "ESCP", "location": json.dumps({"lat": 52.5070, "lon": 13.3278})},
    {"name": "Steinbeis-Hochschule Berlin", "short_name": "SHB", "location": json.dumps({"lat": 52.5023, "lon": 13.3296})},
    {"name": "Bard College Berlin", "short_name": "Bard Berlin", "location": json.dumps({"lat": 52.5678, "lon": 13.4502})},
]

with app.app_context():
    for eintrag in berliner_hochschulen:
        uni = University(**eintrag)
        db.session.add(uni)
    db.session.commit()
    
print("Berliner Hochschulen mit Koordinaten erfolgreich eingefügt.")
