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

class Weeklyannouncements(db.Model):
    __tablename__ = 'weekly_announcements'
    ann_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ann = db.Column(db.Text, nullable=False)

class ParishEventsUpdates(db.Model):
    __tablename__ = 'parish_events_updates'
    Evn_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Evn_Name = db.Column(db.String(255), nullable=False)
    Evn_Date = db.Column(db.Date, nullable=False)
    Evn_Time = db.Column(db.String(255), nullable=False)

class Annoucementcards(db.Model):
    __tablename__ = 'announcement_cards'
    ann_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

class ParishPriests(db.Model):
    __tablename__ = 'parish_priests'
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_incharge = db.Column(db.String(255), nullable=False)
    tenure = db.Column(db.String(255), nullable=False)

class ParishGallery(db.Model):
    __tablename__ = 'gallery_links'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.Text, nullable=False)
