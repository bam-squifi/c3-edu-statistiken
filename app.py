from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////data/app.db"

@app.route("/")
def hello_world():
    return "<p>Hiya, Globe.</p>"

@app.route("/alle")
def all_stats():
    return "<h1>Alle Statistiken</h1>"
