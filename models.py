from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Community(db.Model):
    __tablename__ = 'communities'
    Comm_No = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Comm_Name = db.Column(db.String(255), nullable=False)
    Rep_Name = db.Column(db.String(255), nullable=False)

class Association(db.Model):
    __tablename__ = 'associations'
    Ass_No = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Ass_Name = db.Column(db.String(255), nullable=False)
    Rep_Name = db.Column(db.String(255), nullable=False)

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
