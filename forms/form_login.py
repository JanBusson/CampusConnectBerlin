from flask_wtf import FlaskForm
from wtforms.fields import EmailField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

#Erstellt Login
class CreateLoginForm(FlaskForm):  
    #Felder für die Eingabe beim Login
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')