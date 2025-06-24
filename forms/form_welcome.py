from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField

#Erstellt Login
class CreateWelcomeForm(FlaskForm): 
    #Felder für die Eingabe beim Login
    find_matches = SubmitField('Find Matches')
    # Filter nicht entsprechend dem Sinn der App?
    #TODO etwas in Richtung rate my matches für die Auswertung der Kompatibilität => weights setzen
    set_filters = SubmitField('Set Filters')
    my_matches = SubmitField('My Matches')
    
    