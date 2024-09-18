from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pymysql
import os
from models import db, Annoucementcards, Admin

pymysql.install_as_MySQLdb()
app = Flask(__name__, static_folder = 'design_files')
app.config['SECRET_KEY'] = "\xe0\tC\xfb[\xa62\xdd\xb8pQ\xe6\x8a\xe7\x87\xe7\x94\x0f2\xd0\xe1\xfa\xe9Q\x06a\xab\xecy\x80\x10\xe2"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dsouza@localhost/church_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager(app)
login_manager.login_view = 'login'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

@app.route("/uploads/<path:filename>")
def serve_upload(filename):
    uploads_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    return send_from_directory(uploads_dir, filename)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Admin.query.filter_by(a_name = username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin")
@login_required
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin/cards")
@login_required
def admin_cards():
    cards = Annoucementcards.query.all()
    return render_template("admin_cards.html", cards=cards)

@app.route("/admin/add_card", methods=['GET', 'POST'])
@login_required
def add_card():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        file = request.files['image']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_url = f'uploads/{filename}'
            
            new_card = Annoucementcards(title=title, content=content, image_url=image_url)
            db.session.add(new_card)
            db.session.commit()
            flash('New card added successfully', 'success')
            return redirect(url_for('admin_cards'))
        
    return render_template('add_card.html')

@app.route("/admin/edit_card/<int:card_id>", methods=['GET', 'POST'])
@login_required
def edit_card(card_id):
    card = Annoucementcards.query.get_or_404(card_id)
    if request.method == 'POST':
        card.title = request.form['title']
        card.content = request.form['content']
        file = request.files['image']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            card.image_url = url_for('static', filename=f'uploads/{filename}')
        
        db.session.commit()
        flash('Card updated successfully', 'success')
        return redirect(url_for('admin_cards'))
    
    return render_template('edit_card.html', card=card)

@app.route("/admin/delete_card/<int:card_id>")
@login_required
def delete_card(card_id):
    card = Annoucementcards.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()
    flash('Card deleted successfully', 'success')
    return redirect(url_for('admin_cards'))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)