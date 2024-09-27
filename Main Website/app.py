import pymysql
from flask import Flask, render_template, url_for, send_from_directory
import os
import requests
from bs4 import BeautifulSoup
import random
import re
import json
from flask_sqlalchemy import SQLAlchemy
from models import db, Community, Association, Masstimings, Novena, Weeklyannouncements, ParishEventsUpdates, Annoucementcards, ParishPriests, ParishGallery

pymysql.install_as_MySQLdb()
app = Flask(__name__, static_folder = 'design_files')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dsouza@localhost/church_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def extract_image_urls(soup):
    script_tag = soup.find('script', string=lambda t: t and 'AF_initDataCallback' in t)
    if script_tag:
        match = re.search(r'AF_initDataCallback\((.*?)\);', script_tag.string, re.DOTALL)
        if match:
            json_str = match.group(1)
            json_str = re.sub(r'^.*?\(', '', json_str)
            json_str = re.sub(r'\)$', '', json_str)
            json_str = json_str.strip().rstrip(',')
            data = json.loads(json_str)
            return [item[1][0] for item in data[1] if isinstance(item, list) and len(item) > 1 and isinstance(item[1], list) and len(item[1]) > 0]
    image_divs = soup.find_all('div', {'data-og-image': True})
    if image_divs:
        return [div['data-og-image'] for div in image_divs]
    meta_tags = soup.find_all('meta', property='og:image')
    if meta_tags:
        return [tag['content'] for tag in meta_tags]
    return []

def extract_highlight_image(soup):
    play_button = soup.find('div', class_='RY3tic')
    if play_button:
        style = play_button.get('style')
        if style:
            match = re.search(r'background-image:url\((.*?)\)', style)
            if match:
                return match.group(1)
    og_image = soup.find('meta', property='og:image')
    if og_image:
        return og_image['content']
    return None

@app.route("/hello_world_test")
def hello_world():
    return "<p>Hello World! From Python Flask!<p>"

@app.route('/uploads/<path:filename>')
def serve_upload(filename):
    uploads_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    return send_from_directory(uploads_dir, filename)

@app.route("/")
def homepage():
    masstimes = Masstimings.query.all()
    novenas = Novena.query.all()
    weeklyannouncements = Weeklyannouncements.query.all()
    parish_events_updates = ParishEventsUpdates.query.all()
    cards = Annoucementcards.query.order_by(Annoucementcards.ann_id.desc()).all()
    return render_template("/webpages/home.html", masstimes = masstimes, novenas = novenas, weeklyannouncements = weeklyannouncements, parish_events_updates = parish_events_updates, cards = cards)

@app.route("/history")
def historypage():
    return render_template("/webpages/history.html")

@app.route("/patronsaint")
def patronsaintpage():
    return render_template("/webpages/patronsaint.html")

@app.route("/parishinformation")
def parishinformationpage():
    return render_template("/webpages/parishinformation.html")

@app.route("/previouspriests")
def previouspriestspage():
    parish_priests = ParishPriests.query.all()
    return render_template("/webpages/previouspriests.html", parish_priests = parish_priests)

@app.route("/parishcouncil")
def parishcouncilpage():
    communities = Community.query.all()
    associations = Association.query.all()
    return render_template("/webpages/parishcouncil.html", communities=communities, associations=associations)

@app.route("/parishgallery")
def parishgallery():
    galleries = ParishGallery.query.all()
    for gallery in galleries:
        try:
            response = requests.get(gallery.link)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            highlight_image = extract_highlight_image(soup)
            
            all_image_urls = extract_image_urls(soup)
            
            if highlight_image:
                gallery.thumbnail_url = highlight_image
                if highlight_image not in all_image_urls:
                    all_image_urls.insert(0, highlight_image)
            else:
                print(f"No highlight image found for gallery: {gallery.title}")
                gallery.thumbnail_url = None

            if all_image_urls:
                gallery.image_urls = random.sample(all_image_urls, min(20, len(all_image_urls)))
            else:
                print(f"No images found for gallery: {gallery.title}")
                gallery.image_urls = []

        except Exception as e:
            print(f"Error fetching images for {gallery.title}: {str(e)}")
            gallery.thumbnail_url = None
            gallery.image_urls = []
    return render_template("/webpages/parishgallery.html", galleries = galleries)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)