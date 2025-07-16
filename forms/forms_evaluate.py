from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, HiddenField
from wtforms.validators import InputRequired

class CreateRatingForm(FlaskForm):
    #HiddenField für die Zuordnung Bewertung -> User
    match_id = HiddenField(validators=[InputRequired()])
    rating = RadioField(
        'Rate your match',
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        validators=[InputRequired()],
        coerce=str #=> in String
    )
    submit = SubmitField('Submit')