# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = '£#$#£$#£$#£$343Fa
wd##24'

@app.route("/")
def main():
	return render_template('main.html') 

def check_login(username, password):
	if username == "furkan" and password == "123456":
		session['user'] = "furkan"
		return True
	else:
		return False

@app.route("/login", methods=['POST','GET'])
def login():
        if request.method == 'POST':
		if check_login(request.form['username'], request.form['pass']):
			return redirect(url_for('main')) 
		else:
			return "O iş olmaz"
			


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
