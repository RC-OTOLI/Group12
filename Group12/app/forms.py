from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, InputRequired, Email, Length, EqualTo
from flask_login import current_user
from app.models import User, Transaction
from app import db

"""
forms.py
====================================
Defines the different type of forms and requirements
"""

class LoginForm(FlaskForm):
    """Login Form for Wallet."""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')

    def validate_username(self, username):
        """
        Verify Username is in database

        Parameters
        ---------
        username
            String assigned to name of person

        """
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("Could not find a user with that name!")


class AddForm(FlaskForm):
    """Add Form when adding to transaction."""
    amount = FloatField('Amount', validators=[InputRequired()])
    description = StringField('Description', validators=[Length(min=0, max=80)])
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    """Checkbox for Delete Form"""
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class DeleteForm(FlaskForm):
    """Delete Form when deleting from transaction."""
    transactions = []
    try:
        for t in Transaction.query.filter_by(user_id=current_user.id):
            transactions.append(t.timestamp, t.amount, t.description)
    except:
        pass
    
    fields = MultiCheckboxField('Label', choices=transactions)
    
class RegisterForm(FlaskForm):
    """Register Form for Wallet"""
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('E-mail', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    password2 = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', message="passwords must match")])

    # Uncomment to restrict duplicate usernames
    def validate_username(self, username):
        """
        Verify Username if isn't taken

        Parameters
        ---------
        username
            String assigned to name of person

        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken')

    # Emails must be unique
    def validate_email(self, email):
        """
        Verify Email if isn't taken

        Parameters
        ---------
        username
            String assigned to name of person

        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('That email is already in use')


class MaxBudgetForm(FlaskForm):
    """Set Maximum Budget for Wallet threshhold"""
    max_budget = FloatField('Set max budget: ', validators=[InputRequired()])
