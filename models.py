# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Task', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(
            password,
            method="pbkdf2:sha256",
            salt_length=16
        )

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='not-completed')
    priority = db.Column(db.String(10), default='medium')  # << NEW
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def toggle(self):
        self.status = 'completed' if self.status == 'not-completed' else 'not-completed'

    def __repr__(self):
        return f"<Task id={self.id} title='{self.title}' status={self.status} priority={self.priority}>"
