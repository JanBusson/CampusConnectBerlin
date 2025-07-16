from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField,EmailField, PasswordField, DateField, SelectField, FileField

class CreateChatForm(FlaskForm):  
    message = StringField('Your Message')
    sned_message = SubmitField('Send')