from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Length

#TODO Fehlermeldungen für die einzelnen Validators coden

#Erstellt Login
class CreateLoginForm(FlaskForm):  
    #Felder für die Eingabe beim Login
    first_name = StringField('First Name', [DataRequired(), Length(min=2)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2)])
    #TODO restliche Felder ergänzen
    
    submit = SubmitField('Finish')