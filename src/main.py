
from flask import Flask,render_template,request,session,redirect,url_for
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", 
    
	database="studenti" # napraviti bazu i importovati
    # korisnik.sql u nju 
    )
def uklanjanje_bytearray(podaci):
	podaci = list(podaci)
	n = len(podaci)
	for i in range(n):
		if isinstance(podaci[i], bytearray):
			podaci[i] = podaci[i].decode()
	return podaci
@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	indeks = request.form['indeks']
	ime_prezime = request.form['ime_prezime']
	godina = int(request.form['godina'])
	password = request.form['password']
	confirm = request.form['confirm']
	prosek = float(request.form['prosek'])
	polozeni = int(request.form['polozeni'])

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE broj_indeksa = ?"
	vrednosti = (indeks, )
	cursor.execute(sql,vrednosti)
	rez = cursor.fetchone()

	if rez != None:
		return render_template("register.html", indeks_greska="Student sa ovim indeksom vec postoji!")
	if password != confirm:
		return render_template("register.html", greska_pass="Sifre se ne poklapaju!")
	if prosek <= 6.0 or prosek >= 10.0:
		return render_template("register.html", greska_prosek="Prosek nije u opsegu 6 - 10!")
	if polozeni < 0:
		return render_template("register.html", greska_polozeni="Broj polozenih mora da bude pozitivan!")

	cursor = mydb.cursor(prepared=True)
	sql= "INSERT INTO korisnik VALUES(null, ?, ?, ?, ?, ?, ?)"
	vrednosti = (indeks, ime_prezime, godina, password, prosek, polozeni)
	cursor.execute(sql, vrednosti)
	mydb.commit()
	return redirect(url_for('show_all'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET' and 'indeks' not in session:
		return render_template("login.html")
	elif 'indeks' in session:
		return redirect(url_for("show_all"))

	indeks = request.form['indeks']
	password = request.form['password']

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE broj_indeksa = ?"
	vrednosti = (indeks, )
	cursor.execute(sql, vrednosti)
	rez = cursor.fetchone()

	if rez == None:
		return render_template("login.html", indeks_greska="Student sa ovim indeksom ne postoji!")
	if password != rez[4].decode():
		return render_template("login.html", greska_pass="Sifra nije ispravna!")
	
	session['indeks'] = indeks

	return redirect(url_for('show_all'))

@app.route('/logout')
def logout():
	if 'indeks' in session:
		session.pop('indeks')
		return render_template("login.html")
	else: 
		return redirect(url_for('show_all'))

@app.route('/show_all')
def show_all():
	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik"
	cursor.execute(sql)
	rez = cursor.fetchall()

	n = len(rez)
	for i in range(n):
		rez[i] = uklanjanje_bytearray(rez[i])
	
	return render_template("show_all.html", korisnici = rez)

@app.route('/delete/<indeks>')
def delete(indeks):
	if 'indeks' not in session:
		return render_template("login.html")
	else:
		cursor = mydb.cursor(prepared=True)
		sql = "DELETE FROM korisnik WHERE broj_indeksa = ?"
		vrednosti = (indeks, )
		cursor.execute(sql, vrednosti)
		mydb.commit()
		return redirect(url_for('show_all'))

@app.route('/update/<indeks>', methods=['GET', 'POST'])
def update(indeks):
	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE broj_indeksa = ?"
	vrednosti = (indeks, )
	cursor.execute(sql, vrednosti)
	rez = cursor.fetchone()

	rez = uklanjanje_bytearray(rez)

	if request.method == 'GET':
		return render_template("update.html", korisnik = rez)
	
	ime_prezime = request.form['ime_prezime']
	godina = int(request.form['godina'])
	password = request.form['password']
	confirm = request.form['confirm']
	prosek = float(request.form['prosek'])
	polozeni = int(request.form['polozeni'])

	if password != confirm:
		return "Sifre se ne poklapaju!"
	if prosek <= 6.0 or prosek >= 10.0:
		return "Prosek nije u opsegu 6 - 10!"
	if polozeni < 0:
		return "Broj polozenih mora da bude pozitivan!"
	
	cursor = mydb.cursor(prepared=True)
	sql = "UPDATE korisnik SET ime_prezime = ?, godina_rodjenja = ?, sifra = ?, prosek = ?, polozeni_ispiti = ? WHERE broj_indeksa = ?"
	vrednosti = (ime_prezime, godina, password, prosek, polozeni, indeks)
	cursor.execute(sql, vrednosti)
	mydb.commit()

	return redirect(url_for("show_all"))

@app.route('/better_than_average/<average>', methods=['GET', 'POST'])
def better_than_average(average):
	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE prosek > ?"
	cursor.execute(sql, average)
	rez = cursor.fetchall()

	n = len(rez)
	for i in range(n):
		rez[i] = uklanjanje_bytearray(rez[i])

	return render_template("better_than.html", korisnici = rez, min_prosek = average)

app.run(debug=True)
