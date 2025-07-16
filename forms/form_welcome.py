from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField

#Erstellt Login
class CreateWelcomeForm(FlaskForm): 
    #Felder für die Eingabe beim Login
    find_matches = SubmitField('Find Friends')
    #friend_suggestions = SubmitField('Friend Suggestions')
    my_matches = SubmitField('My Matches')
    my_chats = SubmitField('My Chats')
    evaluate_match = SubmitField('Rate the fit 🤝🔥')
    evaluation_overview = SubmitField('Ealuation Overview 🕵')
    
    