from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

google_blueprint =  make_google_blueprint(client_id='198432854470-8or4s0j1r899khmq0p72fmi4mmj968iq.apps.googleusercontent.com', client_secret='xSKeuuHrbyQKFTg94ADaJH9B')
app.register_blueprint(google_blueprint, url_prefix='/google_login')

@app.route('/google')
def google_login():
	return redirect(url_for('google.login'))
