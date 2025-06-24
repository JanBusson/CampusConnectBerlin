from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

#Lädt Match
class CreateMatchingForm(FlaskForm): 
    submit = SubmitField("Let's Connect")
    submit = SubmitField('Not a Fit')