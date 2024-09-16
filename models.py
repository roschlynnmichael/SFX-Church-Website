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
