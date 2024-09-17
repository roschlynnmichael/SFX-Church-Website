from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import pymysql
from models import db, Annoucementcards, Admin

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dsouza@localhost/church_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/admin/cards")
def admin_cards():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)