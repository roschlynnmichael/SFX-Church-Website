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

class Masstimings(db.Model):
    __tablename__ = 'mass_timings'
    Mass_No = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Mass_Day = db.Column(db.String(255), nullable=False)
    Mass_Time = db.Column(db.String(255), nullable=False)
    Mass_Lang = db.Column(db.String(255), nullable=False)

class Novena(db.Model):
    __tablename__ = 'novenas'
    Nov_No = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nov_Name = db.Column(db.String(255), nullable=False)
    Nov_Day = db.Column(db.String(255), nullable=False)

class Weeklyannouncements(db.Model):
    __tablename__ = 'weekly_announcements'
    ann_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ann = db.Column(db.Text, nullable=False)

class ParishEventUpdates(db.Model):
    __tablename__ = 'parish_events_updates'
    Evn_no = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Evn_Name = db.Column(db.String(255), nullable = False)
    Evn_Date = db.Column(db.Date, nullable = False)
    Evn_Time = db.Column(db.String(255), nullable = False)

class Association(db.Model):
    __tablename__ = 'associations'
    Ass_No = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Ass_Name = db.Column(db.String(255), nullable = False)
    Rep_Name = db.Column(db.String(255), nullable = False)

class Community(db.Model):
    __tablename__ = 'communities'
    Comm_No = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Comm_Name = db.Column(db.String(255), nullable = False)
    Rep_Name = db.Column(db.String(255), nullable = False)

class ParishPriests(db.Model):
    __tablename__ = 'parish_priests'
    p_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    p_incharge = db.Column(db.String(255), nullable = False)
    tenure = db.Column(db.String(255), nullable = False)
    def __repr__(self):
        return f'<ParishPriests {self.p_incharge}>'
    
class Gallery(db.Model):
    __tablename__ = 'gallery_links'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255), nullable = False)
    link = db.Column(db.Text, nullable = False)

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
