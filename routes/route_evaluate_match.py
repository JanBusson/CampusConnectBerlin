from flask import render_template,redirect, url_for, flash, session, request
from . import main_bp
from dao.match_dao import match_dao
from dao.user_dao import user_dao
from forms.forms_evaluate import CreateRatingForm

@main_bp.route('/evaluate_match', methods=['GET', 'POST']) 
def evaluate_match():
    user_id= session.get('user_id')
    currUser = user_dao.get_uid(user_id)
    matches = match_dao.get_all_for_uid(user_id=user_id)
    
    # Prüfen ob POST
    if request.method == 'POST':
        form = CreateRatingForm()
        if form.validate_on_submit():
            match_id = form.match_id.data
            rating = form.rating.data

            # Optional: Logging oder Debugging
            print(f"[INFO] User {user_id} bewertet Match {match_id} mit {rating}")

            # Bewertung speichern – hier müsstest du z. B. match_dao.evaluate_match(...) aufrufen
            match_dao.evaluate_match(user_id=user_id, match_id=match_id, rating=rating)

            flash("Bewertung erfolgreich gespeichert.", "success")
            return redirect(url_for('main.evaluate_match'))

        
    #hier muss die Klasse und nicht Instanz übergeben werden, da für jedes Match ein neues Ratin Form erstellt wird
    return render_template('evaluate_match.html',matches=matches,currUser=currUser,RatingForm=CreateRatingForm)