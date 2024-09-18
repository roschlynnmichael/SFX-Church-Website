from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Annoucementcards(db.Model):
    __tablename__ = 'announcement_cards'
    ann_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin_user'

    a_id = db.Column(db.Integer, primary_key=True)
    a_name = db.Column(db.String(128), unique=True, nullable=False)
    a_pass = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.a_id)

    def set_password(self, password):
        self.a_pass = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.a_pass, password)
