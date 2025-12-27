from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////data/app.db"

@app.route("/")
def hello_world():
    return "<p>Hiya, Globe.</p>"
