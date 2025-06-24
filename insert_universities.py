from db import db
from datetime import date
import base64
from models import University, User
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campusconnect_berlin.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

universities = [
    {"name": "Technische Universität Berlin", "short_name": "TU Berlin", "location": "Berlin"},
    {"name": "Freie Universität Berlin", "short_name": "FU Berlin", "location": "Berlin"},
    {"name": "Humboldt-Universität zu Berlin", "short_name": "HU Berlin", "location": "Berlin"},
    {"name": "Universität der Künste Berlin", "short_name": "UdK Berlin", "location": "Berlin"},
    {"name": "Berliner Hochschule für Technik", "short_name": "BHT Berlin", "location": "Berlin"},
    {"name": "Hochschule für Wirtschaft und Recht Berlin", "short_name": "HWR Berlin", "location": "Berlin"},
    {"name": "Hochschule für Technik und Wirtschaft Berlin", "short_name": "HTW Berlin", "location": "Berlin"},
    {"name": "Alice Salomon Hochschule Berlin", "short_name": "ASH Berlin", "location": "Berlin"},
    {"name": "Evangelische Hochschule Berlin", "short_name": "EHB", "location": "Berlin"},
    {"name": "Kunsthochschule Berlin-Weißensee", "short_name": "KHB Berlin", "location": "Berlin"},
]

with app.app_context():

    # Dummy image data (you could also load actual image bytes)
    dummy_picture = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00'

    # Get example universities
    fu_berlin = University.query.filter_by(short_name="FU Berlin").first()
    tu_berlin = University.query.filter_by(short_name="TU Berlin").first()
    htw_berlin = University.query.filter_by(short_name="HTW Berlin").first()

    # Example users
    example_users = [
        {
            "name": "Lena Müller",
            "email": "lena.mueller@example.com",
            "password": "secure123",  # in real apps: use hashing!
            "birth_date": date(1998, 5, 20),
            "created_at": date.today(),
            "profile_picture": dummy_picture,
            "description": "Loves psychology and art.",
            "uni_id": fu_berlin.uni_id if fu_berlin else None
        },
        {
            "name": "Tom Schneider",
            "email": "tom.schneider@example.com",
            "password": "password456",
            "birth_date": date(1997, 9, 13),
            "created_at": date.today(),
            "profile_picture": dummy_picture,
            "description": "Aspiring engineer and part-time musician.",
            "uni_id": tu_berlin.uni_id if tu_berlin else None
        },
        {
            "name": "Anna Fischer",
            "email": "anna.fischer@example.com",
            "password": "pass789",
            "birth_date": date(2000, 1, 5),
            "created_at": date.today(),
            "profile_picture": dummy_picture,
            "description": "Interested in social sciences and volunteering.",
            "uni_id": htw_berlin.uni_id if htw_berlin else None
        }
    ]

    # Insert into the database
    for data in example_users:
        user = User(**data)
        db.session.add(user)

    db.session.commit()

    print("Example users inserted successfully.")