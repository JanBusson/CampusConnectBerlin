from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

#Lädt Match
class CreateMatchingForm(FlaskForm): 
    yes = SubmitField("Let's Connect")
    no = SubmitField('Not a Fit')