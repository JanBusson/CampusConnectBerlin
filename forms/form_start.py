from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

#Erstellt Login
class CreateStartForm(FlaskForm):  
    #Auswahl
    login = SubmitField('Login')
    register = SubmitField('Register')
    
    