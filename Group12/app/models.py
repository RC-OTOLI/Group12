from datetime import datetime
from app import db
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

"""
models.py
====================================
Contains data to store
"""

class User(UserMixin, db.Model):
    """Stores data for all fields."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    max_budget = db.Column(db.Float(), nullable=False, default=0.00)
    transactions = db.relationship('Transaction', backref='author', lazy='dynamic')

    # called in routes.py
    # makes sure the hash is stored, not the plaintext
    def set_password(self, password):
        """
        Set hash when creating new password

        Parameters
        ---------
        password
            String assigned to password of account

        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify password is identical

        Parameters
        ---------
        password
            String assigned to password of account

        """
        return check_password_hash(self.password_hash, password)

    def set_max_budget(self, max_budget):
        """
        Set Max Budget for personal transaction threshold

        Parameters
        ---------
        max_budget
            Float assigned to personal threshold

        """
        self.max_budget = max_budget

    def get_max_budget(self):
        """Return Max Budget"""
        return self.max_budget

    #basic representation
    def __repr__(self):
        """Hash visual for Username"""
        return '\n<id: {}, Username: {}>'.format(self.id, self.username)    

    #full representation sans hash
    def full_detail(self):
        """Hash for User"""
        return '\n<User id: {}, Username: {}, Email: {}, Max budget: {}>'.format(self.id, self.username, self.email, self.max_budget)


class Transaction(db.Model):
    """Stores data for all transactions, ."""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(144))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # basic representation
    def __repr__(self):
        return '\n<Transaction UID: {} | amt: {} ; {}>'.format(self.user_id, self.amount, self.description)

    # full representation
    def full_detail(self):
        return '\n<Transaction UID: {} | id: {} | amt: {} ; {} at: {} >'.format(self.user_id, self.id, self.amount, self.description, self.timestamp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))