from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,PasswordField
from wtforms.validators import ValidationError, InputRequired, Email, Length, EqualTo
from app.models import User

class AddForm(FlaskForm):
    amount = IntegerField('username', validators=[InputRequired(), Length(min=0, max=15)])
    description = StringField('password', validators=[InputRequired(), Length(min=0, max=80)])
   
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    password2 = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password', message="passwords must match")])

    # Uncomment to restrict duplicate usernames
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Username is already taken')

    # Emails must be unique
   