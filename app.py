from flask import Flask, render_template

app = Flask(__name__, static_folder = 'design_files')

@app.route("/hello_world_test")
def hello_world():
    return "<p>Hello World! From Python Flask!<p>"

@app.route("/")
def homepage():
    return render_template("/webpages/home.html")

@app.route("/history")
def historypage():
    return render_template("/webpages/history.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)