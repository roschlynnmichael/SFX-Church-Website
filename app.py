import pymysql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Community, Association, Masstimings, Novena, Weeklyannouncements, ParishEventsUpdates

pymysql.install_as_MySQLdb()
app = Flask(__name__, static_folder = 'design_files')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dsouza@localhost/church_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/hello_world_test")
def hello_world():
    return "<p>Hello World! From Python Flask!<p>"

@app.route("/")
def homepage():
    masstimes = Masstimings.query.all()
    novenas = Novena.query.all()
    weeklyannouncements = Weeklyannouncements.query.all()
    parish_events_updates = ParishEventsUpdates.query.all()
    return render_template("/webpages/home.html", masstimes = masstimes, novenas = novenas, weeklyannouncements = weeklyannouncements, parish_events_updates = parish_events_updates)

@app.route("/history")
def historypage():
    return render_template("/webpages/history.html")

@app.route("/patronsaint")
def patronsaintpage():
    return render_template("/webpages/patronsaint.html")

@app.route("/parishcouncil")
def parishcouncilpage():
    communities = Community.query.all()
    associations = Association.query.all()
    return render_template("/webpages/parishcouncil.html", communities=communities, associations=associations)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)