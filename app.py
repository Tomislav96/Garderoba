from flask import Flask, Response, request, flash, render_template, current_app, redirect
from baza import Ormar, Stalak_za_obucu
import sqlite3
import secrets
import os

db = sqlite3.connect("baza.sqlite", check_same_thread=False)

app = Flask(__name__)

cur = db.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ormar', methods=['GET', 'POST'])
def ormar():
	if request.method == 'POST':
		naziv = request.form.get('naziv')
		velicina = request.form.get('velicina')
		vlasnik = request.form.get('vlasnik')
		datum = request.form.get('datum')
		db.execute("INSERT INTO Ormar(naziv,velicina,vlasnik, datum) VALUES (:naziv,:velicina,:vlasnik, :datum)", {"naziv":naziv,"velicina":velicina,"vlasnik":vlasnik, "datum":datum})
		db.commit()
		return render_template('ormar.html')
	return render_template('ormar.html')


@app.route('/pokazi', methods=['GET', 'POST'])
def pokazi():
	if request.method == 'POST':
		print("radi")
		ime = request.form.get('ime')
		
		ime1 = request.form.get('ime1')
		print(ime)
		print(ime1)
		if ime != None:
			db.execute("DELETE FROM Ormar WHERE id="+ime+"")
			db.commit()
		if ime1 != None:
			db.execute("DELETE FROM Stalak_za_obucu WHERE id="+ime1+"")
			db.commit()
		
	cur.execute("select * from Ormar")
	data = cur.fetchall()
	cur.execute("select * from Stalak_za_obucu")
	data1 = cur.fetchall()
	return render_template('pokazi.html', value=data, value1=data1)

@app.route('/stalak', methods=['GET', 'POST'])
def stalak():
	if request.method == 'POST':
		naziv = request.form.get('naziv')
		velicina = request.form.get('velicina')
		vlasnik = request.form.get('vlasnik')
		datum = request.form.get('datum')
		db.execute("INSERT INTO Stalak_za_obucu(naziv,velicina,vlasnik, datum) VALUES (:naziv,:velicina,:vlasnik, :datum)", {"naziv":naziv,"velicina":velicina,"vlasnik":vlasnik, "datum":datum})
		db.commit()
		return render_template('stalak.html')
	return render_template('stalak.html')
if __name__ == "__main__":
	app.run(debug=True)
