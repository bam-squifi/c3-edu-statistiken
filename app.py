from flask import Flask, request, render_template
from markupsafe import escape
from db import get_db, truncate_db
import sqlite3, click, datetime

app = Flask(__name__)

app.config['DATABASE'] = 'c3-edu.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from stats")
    rows = cur.fetchall()
    return [dict(row) for row in rows]

@app.route('/stats/<bundesland>')
def show_stats_for_bundesland(bundesland):
    db = get_db()
    cur = db.cursor()
    state = escape(bundesland)
    cur.execute("select * from stats where state = ?", (state,))
    rows = cur.fetchall()
    return [dict(row) for row in rows]



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
                state,
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
    db.close()
    return "Ok - check your terminal output"

@app.route('/deletedata')
def delete_data():
    truncate_db()
    return "Data - successfully deleted"
    
