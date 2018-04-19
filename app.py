import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired
from flask_migrate import Migrate
import json
import random
from random import shuffle
# from OAuth import google_login
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
app.config['SECRET_KEY'] = 
app.config['SQLALCHEMY_DATABASE_URI'] = 


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

'''
Create Tables
-------------
Form Data
'''
# Store all form responses in a table
class FormResponses(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.Integer) 										#User: unique identifier
	variant = db.Column(db.Integer, db.ForeignKey('variants.id'))										#Variant: name of INS and DEL chr:start coordinate and end coordinate
	q1_answer = db.Column(db.Integer, db.ForeignKey('q1_answer.id'))	#Q1 Answer: a number/int representing genotype
	q2_answer = db.Column(db.Integer, db.ForeignKey('q2_answer.id'))	#Q2 Answer: a number/int representing GT certainty
	q3_answer = db.Column(db.Integer, db.ForeignKey('q3_answer.id'))	#Q3 Answer: a number/int representing base quality
	q4_answer = db.Column(db.String(5000))								#Q4 Answer: a text field made available to list additional description of difficult variants
	q5_answer = db.Column(db.Integer, db.ForeignKey('q5_answer.id'))


# Store the responses to each question in an individual table
# These are only created because there are multiple options for each question
class q1_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	responses = db.relationship('FormResponses', backref='q1_answer_ref', lazy=True)

class q2_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	responses = db.relationship('FormResponses', backref='q2_answer_ref', lazy=True)

class q3_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	responses = db.relationship('FormResponses', backref='q3_answer_ref', lazy=True)

class q5_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	responses = db.relationship('FormResponses', backref='q5_answer_ref', lazy=True)



'''
Create Tables
-------------
Variant Data
'''
class Variants(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	del_ins = db.Column(db.String(50))
	variant_name = db.Column(db.String(5000))
	variant_size = db.Column(db.Integer)
	variant_id = db.Column(db.String(50000))
	image_name = db.Column(db.String(5000))
	igv_image = db.Column(db.String(50000))
	gEval_image = db.Column(db.String(50000))
	svviz_DotPlot_image = db.Column(db.String(50000))
	svviz_PB_image = db.Column(db.String(50000))
	svviz_Ill250_image = db.Column(db.String(50000))
	svviz_Ill300x_image = db.Column(db.String(50000))
	svviz_10X_image = db.Column(db.String(50000))
	svviz_MP_image = db.Column(db.String(50000))

'''
Create a Users Table
'''
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	google_id = db.Column(db.Integer, unique=True)
	user_variants = db.Column(db.String(10000))


class OAuth(OAuthConsumerMixin, db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey(User.id))
	user = db.relationship(User)



'''
Form
----
Code that displays the form options on the front end
'''

class MyForm(FlaskForm):
	# radios = RadioField('Radios', choices=[('Homozygous Reference', 'Homozygous Reference'),('Heterozygous Variant', 'Heterozygous Variant'),('Homozygous Variant','Homozygous Variant'),('Complex [ie: 2+ variants in this region] or difficult', 'Complex [ie: 2+ variants in this region] or difficult')])
	radios = RadioField(choices=[('1', 'Yes [Answer Q3 and Q4]'),('2', 'No[Answer Q2 only]')])
	radios2 = RadioField(choices=[('1', 'Yes'),('2', 'No')])
	radios3 = RadioField(choices=[('1', 'Homozygous Reference'),('2', 'Heterozygous Variant'),('3','Homozygous Variant'),('4', 'Complex [ie: 2+ variants in this region] or difficult')])
	radios4 = RadioField(choices=[('1', '2 [most confident]'),('2', '1'),('3','0 [least confident]')])

google_blueprint =  make_google_blueprint(redirect_to='start_variant', client_id='', client_secret='')
app.register_blueprint(google_blueprint, url_prefix='/google_login')
# google_blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/google')
def google_login():
	if not google.authorized:
		return redirect(url_for('google.login'))
	account_info = google.get('oauth2/v2/userinfo')

	if account_info.ok:
	    account_info_json = account_info.json()
	print (account_info.text)
	print (account_info.json()['id'])
	return render_template('index.html')

@oauth_authorized.connect_via(google_blueprint)
def google_logged_in(blueprint, token):
	account_info = blueprint.session.get('oauth2/v2/userinfo')

	if account_info.ok:
		account_info_json = account_info.json()
		google_id = account_info.json()['id']
		query = User.query.filter_by(google_id=google_id)
		try:
			user = query.one()
		except NoResultFound:
			rand_list = [[i] for i in range(1,5)]
			shuffle(rand_list)
			user = User(google_id=google_id, user_variants=json.dumps(rand_list))
			db.session.add(user)
			db.session.commit()
		login_user(user)

@app.route('/survey')
def start_variant():
	id = json.loads(current_user.user_variants)[0]
	variant_info = Variants.query.get(id)
	return redirect(url_for('index', variant_id=variant_info.variant_id))

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/<string:variant_id>', methods=['GET', 'POST'])
@login_required
def index(variant_id):
	# print(Variants.query.filter_by(variant_id=variant_id).first())
	variant_info = Variants.query.filter_by(variant_id=variant_id).first()
	variant_response = FormResponses.query.filter_by(variant=variant_info.id).filter_by(user=current_user.id).first()
	user_responses = FormResponses.query.filter_by(user=current_user.id).all()
	variant_table = Variants.query.all()
	bar_complete = FormResponses.query.filter_by(user=current_user.id).count() #counts the number of completed survey questions (rows in the FormResponses table)
	bar_total = Variants.query.count()
	bar_percent_complete = (bar_complete/bar_total)*100
	# Find 20% of the size of the variant
	var_size = variant_info.variant_size
	var_size_20 = (var_size)*0.2
	var_plus_20 = int(var_size+var_size_20)
	var_minus_20 = int(var_size-var_size_20)

	# print(Variants.query.outerjoin(FormResponses).filter(FormResponses.variant is None).order_by(db.func.random()).first())

	####
	#Shuffle the order of variants in an array
	####
	#First: Shuffle everyting in the variant table
	shuffle(variant_table)
	# print(variant_table)
	#Second: Print a list of ids for each variant; LMC: variant.id is information coming from the 'variant_table'
	# variant_list = [variant.id for variant in variant_table]
	variant_list = [3,4,2,1]

	# variant_list = [variant.id for variant in shuffle(variant_table)] <-- Incorrect
	print(variant_list)


	if variant_response:
		form = MyForm(radios=variant_response.q1_answer, radios2=variant_response.q2_answer, radios3=variant_response.q3_answer, radios4=variant_response.q5_answer)
	else:
		form = MyForm()

	if request.method == 'POST':
		if variant_response:
		    variant_response.q1_answer = form.radios.data
		    variant_response.q2_answer = form.radios2.data
		    variant_response.q3_answer = form.radios3.data
		    variant_response.q5_answer = form.radios4.data

		else:
		    variant_response = FormResponses(user=current_user.id, variant=variant_info.id, q1_answer=form.radios.data, q2_answer=form.radios2.data, q3_answer=form.radios3.data, q5_answer=form.radios4.data)
		    db.session.add(variant_response)
		db.session.commit()

		if request.form['variantsubmit'] == 'left':
			previous_variant_id = variant_list[variant_list.index(variant_info.id) - 1]
			previous_variant = Variants.query.get(previous_variant_id)
			return redirect(url_for('index', variant_id=previous_variant.variant_id))
		else:
			try:
				next_variant_id = variant_list[variant_list.index(variant_info.id) + 1]
			except IndexError:
				next_variant_id = variant_list[0]
			next_variant = Variants.query.get(next_variant_id)
			return redirect(url_for('index', variant_id=next_variant.variant_id))

	disable_next = False
	if variant_info.id == Variants.query.count():
		disable_next = True

	return render_template('index.html', bar_complete=bar_complete, bar_total=bar_total, bar_percent_complete=bar_percent_complete, var_plus_20=var_plus_20, var_minus_20=var_minus_20, form=form, variant_info=variant_info, disable_next=disable_next, user_responses=user_responses, variant_table=variant_table)

if __name__ == '__main__':
	app.run(debug=True)