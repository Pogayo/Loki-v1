from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField, RadioField

from wtforms.validators import DataRequired
from wtforms import validators


class LoginForm(Form):

    email = StringField("Email", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="Please Fill This Field")])

    password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])

class TransValidateForm(Form):
    example = RadioField('I want to be a ...', choices=[('Translator','Translator'),('Validator','Validator')],
        validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])


class RegisterForm(Form):
    
    name = StringField("Full names", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])
    
    username = StringField("Username", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])
    
    email = StringField("Email", validators=[validators.Email(message="Please enter a valid email address"), validators.DataRequired(message="Please Fill This Field"),])
    
    password = PasswordField("Password", validators=[validators.Length(min=8, max=25, message="Password must be between 8 and 25 characters long"), 
     validators.DataRequired(message="Please Fill This Field"),
     validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")]
     )
    
    confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])
class ValidateForm(Form):

    isValid= RadioField('Is the above translation correct', choices=[('True','True'),('False','False')],
        validators=[validators.DataRequired(message="Please Fill This Field")])