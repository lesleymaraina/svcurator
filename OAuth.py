from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

google_blueprint =  make_google_blueprint(client_id=' ', client_secret=' ')
app.register_blueprint(google_blueprint, url_prefix='/google_login')

@app.route('/google')
def google_login():
	return redirect(url_for('google.login'))
