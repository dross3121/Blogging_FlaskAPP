# Home page routes
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')

@app.route('/login', methods=["GET", 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember.data))
		return redirect(url_for('index'))
	return  render_template("login.html", title="Sign In", form=form)

@app.route('/index')

def index():
	user = {'username': 'Shakasia'}
	post =[
	{	

		'author': {'username': 'Charli'},
		'body': "I'm a baby i'm always hungry!"
	},
	{   'author': {'username': 'Deshawn'},
		'body': "I'm always feeding Charli"
	}	

	]
	return render_template('index.html', title="Home", user=user, posts=post)
