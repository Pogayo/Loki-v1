from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField, RadioField

from wtforms.validators import DataRequired
from wtforms import validators


class LoginForm(Form):

    email = StringField("Email", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="Please Fill This Field")])

    password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])

class TransValidateForm(Form):
    example = RadioField('I want to be a ...', choices=[('Translator','You can translate a sentences'),('Validator','You can validate peoples translations')],
        validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])


class RegisterForm(Form):
    
    name = StringField("Full names", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])
    
    username = StringField("Username", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])
    
    email = StringField("Email", validators=[validators.Email(message="Please enter a valid email address")])
    
    password = PasswordField("Password", validators=[
    
        validators.DataRequired(message="Please Fill This Field"),
    
        validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")
    ])
    
    confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])