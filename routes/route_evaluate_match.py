from flask import render_template,redirect, url_for, flash, session, request
from . import main_bp
from dao.match_dao import match_dao
from dao.user_dao import user_dao
from forms.forms_evaluate import CreateRatingForm

@main_bp.route('/evaluate_match', methods=['GET', 'POST'])
def evaluate_match():
    user_id = session.get('user_id')
    currUser = user_dao.get_uid(user_id)
    matches = match_dao.get_all_for_uid(user_id=user_id)

 
    if request.method == 'POST':
        form = CreateRatingForm(request.form)
        if form.validate_on_submit():
            match_id = form.match_id.data
            rating = form.rating.data
            match_dao.evaluate_match(user_id=user_id, match_id=match_id, rating=rating)
            flash("Bewertung gespeichert.", "success")
            return redirect(url_for('main.evaluate_match'))
        else:
            print("Fehler:", form.errors)

    
    match_forms = []
    for match in matches:
        form = CreateRatingForm()
        form.match_id.data = str(match.match_id)
        match_forms.append((match, form))

    return render_template("evaluate_match.html", match_forms=match_forms, currUser=currUser)
