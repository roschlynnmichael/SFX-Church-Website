from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pymysql
import datetime
import os
from models import db, Annoucementcards, Admin, Masstimings, Novena, Weeklyannouncements, ParishEventUpdates

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
    try:
        with db.session.begin_nested():
            card = Annoucementcards.query.get_or_404(card_id)
            if card.image_url:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], card.image_url.split('/')[-1])
                if os.path.exists(image_path):
                    os.remove(image_path)
            db.session.delete(card)
            remaining_cards = Annoucementcards.query.filter(Annoucementcards.ann_id > card_id).order_by(Annoucementcards.ann_id).all()
            for index, remaining_card in enumerate(remaining_cards):
                remaining_card.ann_id = index
        db.session.commit()
        if Annoucementcards.query.count() == 0:
            with db.engine.connect() as conn:
                conn.execute(text("ALTER TABLE announcement_cards AUTO_INCREMENT = 1"))
        flash('Card deleted successfully and refactored IDs', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting card: {str(e)}', 'error')
    return redirect(url_for('admin_cards'))

# Mass Timings CRUD operations
@app.route("/admin/mass_timings")
@login_required
def admin_mass_timings():
    mass_timings = Masstimings.query.all()
    return render_template("admin_mass_timings.html", mass_timings=mass_timings)

@app.route("/admin/add_mass_timing", methods=['GET', 'POST'])
@login_required
def add_mass_timing():
    if request.method == 'POST':
        new_mass = Masstimings(
            Mass_Day=request.form['Mass_Day'],
            Mass_Time=request.form['Mass_Time'],
            Mass_Lang=request.form['Mass_Lang']
        )
        db.session.add(new_mass)
        db.session.commit()
        flash('New Mass Timing added successfully', 'success')
        return redirect(url_for('admin_mass_timings'))
    return render_template("add_mass_timing.html")

@app.route("/admin/edit_mass_timing/<int:Mass_No>", methods=['GET', 'POST'])
@login_required
def edit_mass_timing(Mass_No):
    mass = Masstimings.query.get_or_404(Mass_No)
    if request.method == 'POST':
        mass.Mass_Day = request.form['Mass_Day']
        mass.Mass_Time = request.form['Mass_Time']
        mass.Mass_Lang = request.form['Mass_Lang']
        db.session.commit()
        flash('Mass Timing updated successfully', 'success')
        return redirect(url_for('admin_mass_timings'))
    return render_template("edit_mass_timing.html", mass=mass)

@app.route("/admin/delete_mass_timing/<int:Mass_No>")
@login_required
def delete_mass_timing(Mass_No):
    mass = Masstimings.query.get_or_404(Mass_No)
    db.session.delete(mass)
    db.session.commit()
    flash('Mass Timing deleted successfully', 'success')
    return redirect(url_for('admin_mass_timings'))

@app.route("/admin/weekly_announcements")
@login_required
def admin_weekly_announcements():
    announcements = Weeklyannouncements.query.all()
    return render_template("admin_weekly_announcements.html", announcements=announcements)

@app.route("/admin/add_weekly_announcement", methods=['GET', 'POST'])
@login_required
def add_weekly_announcement():
    if request.method == 'POST':
        announcement = request.form['announcement']
        new_announcement = Weeklyannouncements(ann=announcement)
        db.session.add(new_announcement)
        db.session.commit()
        flash('New weekly announcement added successfully', 'success')
        return redirect(url_for('admin_weekly_announcements'))
    return render_template("add_weekly_announcement.html")

@app.route("/admin/edit_weekly_announcement/<int:ann_no>", methods=['GET', 'POST'])
@login_required
def edit_weekly_announcement(ann_no):
    announcement = Weeklyannouncements.query.get_or_404(ann_no)
    if request.method == 'POST':
        announcement.ann = request.form['announcement']
        db.session.commit()
        flash("Edit successful", 'success')
        return redirect(url_for('admin_weekly_announcements'))
    return render_template("edit_weekly_announcement.html", announcement=announcement)

@app.route("/admin/delete_weekly_announcement/<int:ann_no>")
@login_required
def delete_weekly_announcement(ann_no):
    announcement = Weeklyannouncements.query.get_or_404(ann_no)
    db.session.delete(announcement)
    db.session.commit()
    flash("Deletion successful", 'success')
    return redirect(url_for('admin_weekly_announcements'))

@app.route("/admin/novenas")
@login_required
def admin_novenas():
    novenas = Novena.query.all()
    return render_template("admin_novenas.html", novenas=novenas)

@app.route("/admin/add_novena", methods=['GET', 'POST'])
@login_required
def add_novena():
    if request.method == 'POST':
        new_novena = Novena(
            Nov_Name=request.form['Nov_Name'],
            Nov_Day=request.form['Nov_Day']
        )
        db.session.add(new_novena)
        db.session.commit()
        flash('New Novena added successfully', 'success')
        return redirect(url_for('admin_novenas'))
    return render_template("add_novena.html")

@app.route("/admin/edit_novena/<int:Nov_No>", methods=['GET', 'POST'])
@login_required
def edit_novena(Nov_No):
    novena = Novena.query.get_or_404(Nov_No)
    if request.method == 'POST':
        novena.Nov_Name = request.form['Nov_Name']
        novena.Nov_Day = request.form['Nov_Day']
        db.session.commit()
        flash('Novena updated successfully', 'success')
        return redirect(url_for('admin_novenas'))
    return render_template("edit_novena.html", novena=novena)

@app.route("/admin/delete_novena/<int:Nov_No>")
@login_required
def delete_novena(Nov_No):
    novena = Novena.query.get_or_404(Nov_No)
    db.session.delete(novena)
    db.session.commit()
    flash('Novena deleted successfully', 'success')
    return redirect(url_for('admin_novenas'))

@app.route("/admin/parish_events")
@login_required
def admin_parish_events():
    events = ParishEventUpdates.query.all()
    return render_template("admin_parish_events.html", events=events)

@app.route("/admin/add_parish_event", methods=['GET', 'POST'])
@login_required
def add_parish_event():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_time = request.form['event_time']
        new_event = ParishEventUpdates(
            Evn_Name = event_name,
            Evn_Date = event_date,
            Evn_Time = event_time
        )
        db.session.add(new_event)
        db.session.commit()
        flash('New Parish Event added successfully', 'success')
        return redirect(url_for('admin_parish_events'))
    return render_template("add_parish_event.html")

@app.route("/admin/edit_parish_event/<int:Evn_no>", methods=['GET', 'POST'])
@login_required
def edit_parish_event(Evn_no):
    event = ParishEventUpdates.query.get_or_404(Evn_no)
    if request.method == 'POST':
        event.Evn_Name = request.form['event_name']
        event.Evn_Date = datetime.strptime(request.form['event_date'], '%Y-%m-%d').date()
        event.Evn_Time = request.form['event_time']
        db.session.commit()
        flash('Parish Event updated successfully', 'success')
        return redirect(url_for('admin_parish_events'))
    return render_template("edit_parish_event.html", event=event)

@app.route("/admin/delete_parish_event/<int:Evn_no>")
@login_required
def delete_parish_event(Evn_no):
    event = ParishEventUpdates.query.get_or_404(Evn_no)
    db.session.delete(event)
    db.session.commit()
    flash('Parish Event deleted successfully', 'success')
    return redirect(url_for('admin_parish_events'))
        

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)