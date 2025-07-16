from flask import render_template
from . import main_bp
from models import Match, User
from db import db
from sqlalchemy.orm import aliased

@main_bp.route("/evaluation_overview")
def evaluation_overview():
    # Erstelle Aliase für User1 und User2
    User1 = aliased(User)
    User2 = aliased(User)

    # Query zur Verknüpfung der Matches mit beiden Benutzern
    matches = db.session.query(
        Match.match_id,
        Match.compatibility,
        Match.rating_by_user1,
        Match.rating_by_user2,
        User1.name.label("user1_name"),
        User2.name.label("user2_name")
    ).join(User1, Match.user1_id == User1.user_id) \
     .join(User2, Match.user2_id == User2.user_id) \
     .all()

    return render_template("evaluation_overview.html", matches=matches)
