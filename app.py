from flask import Flask, request, render_template
from markupsafe import escape
from db import get_db
import sqlite3
import click

app = Flask(__name__)

app.config['DATABASE'] = 'c3-edu.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def submit():
    gender = request.form.get("gender")
    bundesland = request.form.get("bundesland")
    freistellung  = request.form.get("freistellung")
    beruflicheQualifikation  = request.form.get("beruflicheQualifikation")
    bildung = request.form.get("bildung")
    nationalitaet = request.form.get("nationalitaet")
    alter = request.form.get("alter")
    betriebstatus = request.form.get("betriebstatus")
    betriebsgroesse = request.form.get("betriebsgroesse")
    beschaeftigungssektor = request.form.get("beschaeftigungssektor")
    print("Received gender:", gender)
    print("Received:", bundesland)
    print("Received:", freistellung)
    print("Received:", beruflicheQualifikation)
    print("Received:", bildung)
    print("Received:", nationalitaet)
    print("Received:", alter)
    print("Received:", betriebstatus)
    print("Received:", betriebsgroesse)
    print("Received:", beschaeftigungssektor)
    db = get_db()
    cur = db.cursor()
    cur.execute(
        """ INSERT INTO
            stats (
                gender,
                state_id,
                fType,
                qualification,
                degree,
                nationality,
                ageRange,
                jobType,
                jobSize,
                jobArea)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (gender, bundesland,
            freistellung,beruflicheQualifikation,bildung,nationalitaet,alter,betriebstatus,betriebsgroesse,beschaeftigungssektor))
    db.commit()
    return "Ok - check your terminal output"


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
