from datetime import datetime
from app import db
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    transactions = db.relationship('Transaction', backref='author', lazy='dynamic')

    # called in routes.py
    # makes sure the hash is stored, not the plaintext
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)    
        # return '<User {}, {}>'.format(self.username, self.email)

# if db is not initialized yet:
# db.create_all()
# admin = User(username='admin', email='admin@example.com', password='asdf', image_file='asfd') 
# db.session.add(admin) 
# User.query.all()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ammount = db.Column(db.Numeric(precision=2), nullable=False)
    description = db.Column(db.String(144))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Transaction {}: {} | {}>'.format(self.user_id, self.ammount, self.description)
        # return '<{} | {} | {}: {} | {}>'.format(self.user_id, self.id, self.ammount, self.description, self.timestamp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))