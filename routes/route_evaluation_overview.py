from flask import render_template
from . import main_bp
from models import Match, User
from db import db

@main_bp.route("/evaluation_overview")
def evaluation():
    #Erstellung eines Querys für die Vernüpfung für die Matches: Score von Usern <-> Predicted Fit
    matches = db.session.query(
        Match.match_id,
        Match.compatibility,
        Match.rating_by_user1,
        Match.rating_by_user2,
        User.name.label("user1_name"),
        User2.name.label("user2_name")
    ).join(User, Match.user1_id == User.user_id) \
     .join(User2 := User, Match.user2_id == User2.user_id) \
     .all()

    return render_template("evaluation.html", matches=matches)
