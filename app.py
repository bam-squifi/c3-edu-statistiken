from flask import Flask, request, render_template, flash, url_for
from markupsafe import escape
from db import get_db, truncate_db
import sqlite3, click, datetime, secrets, csv

app = Flask(__name__)
app.secret_key = secrets.token_bytes(32)

app.config['DATABASE'] = 'c3-edu.db'

@app.route('/list')
def list():
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from stats")
    rows = cur.fetchall()
    data = [dict(row) for row in rows]
    return render_template("stats.html", data=data, title=f"Alle Statistiken")

@app.route('/stats/<bundesland>')
def show_stats_for_bundesland(bundesland):
    db = get_db()
    cur = db.cursor()
    state = escape(bundesland)
    cur.execute("select * from stats where state = ?", (state,))
    rows = cur.fetchall()
    data = [dict(row) for row in rows]
    return render_template("stats.html", data=data, title=f"Statistiken für {bundesland}")



@app.route('/', methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
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
        flash(f'Die Daten wurden erfolgreich gespeichert!')
    return render_template('index.html')

@app.route('/deletedata')
def delete_data():
    truncate_db()
    return f"Ok - Daten wurden gelöscht"
    
