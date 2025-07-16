from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField

#Erstellt Login
class CreateWelcomeForm(FlaskForm): 
    #Felder für die Eingabe beim Login
    find_matches = SubmitField('Find Matches')
    #friend_suggestions = SubmitField('Friend Suggestions')
    my_matches = SubmitField('My Matches')
    my_chats = SubmitField('My Chats')
    
    