from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import ValidationError, InputRequired, Email, Length, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class AddForm(FlaskForm):
    amount = FloatField('amount', validators=[InputRequired()])
    description = StringField('description', validators=[Length(min=0, max=80)])
    submit = SubmitField('Submit')

    
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    password2 = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password', message="passwords must match")])

    # Uncomment to restrict duplicate usernames
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken')

    # Emails must be unique
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('That email is already in use')


class MaxBudgetForm(FlaskForm):
    max_budget = FloatField('Set max budget', validators=[InputRequired()])
