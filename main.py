# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '£#$#£$#£$#£$343Fa'
db = SQLAlchemy(app)

class Zaafiyet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	aciklama = db.Column(db.String(100), unique=False)
	
	def __init__(self, aciklama):
		self.aciklama = aciklama
	
	def __repr__(self):
		return '<Zaafiyet %r>' % self.aciklama

@app.route("/")
def main():
	return render_template('main.html') 

def check_login(username, password):
	if username == "furkan" and password == "123456":
		return True
	else:
		return False

@app.route("/site")
def iceri():
	try:
		if session['logged_in'] == True:
	 		return session['username']
	except KeyError:
		return "Defol"

@app.route("/login", methods=['POST','GET'])
def login():
        if request.method == 'POST':
		if check_login(request.form['username'], request.form['pass']):
			session['logged_in'] = True
			session['username'] = request.form['username'] 
			return redirect(url_for('iceri')) 
		else:
			return "O iş olmaz"
			


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
