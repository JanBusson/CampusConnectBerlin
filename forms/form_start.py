from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

#Erstellt Login
class CreateStartForm(FlaskForm):  
    #Felder für die Eingabe beim Login
    login = SubmitField('Login')
    register = SubmitField('Register')
    
    