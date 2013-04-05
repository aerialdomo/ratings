from flask import Flask, render_template, redirect, url_for, flash, session, request, g
import model
# import urllib
import requests
app = Flask(__name__)

#Should do a better secret key in the future
app.secret_key = 'teapot'

@app.route("/")
def index():
	user_list = model.session.query(model.User).limit(5).all()
	return render_template("user_list.html", users=user_list)

@app.route("/signup")
def signup():
	pass
	"""
	- method = post
	- a form with user email, password (id is automatically generated)
	- contents of form are submitted
	- user is redirected to authentication page
	"""

@app.route("/login")
def login():
	#does not need code in here, the form data in login.html will pass to /authenticate
	return render_template("login.html", )

@app.route('/authenticate', methods=["POST"])	
def authenticate():
	#this is the data that is passed in from login.html form
	form_password = request.form['password']
	form_uid = request.form['id']
	#querying row from db so that we can compare form data to existing data
	row = model.session.query(model.User).filter_by(id = form_uid).one()
	#we converted form_uid and row.id to int
	#NEED TO FIX LATER
	if (form_password == row.password) and (int(form_uid) == int(row.id)):
		#session is a GLOBAL Flask dictionary object, will save key:values across fuctions
		session['uid'] = row.id
		#url_for builds url to a specific function
		return redirect(url_for('list_movies_by_user',))
	else:
		#flash("Please enter a valid id and password.")
		return redirect(url_for("crash_and_burn"))

@app.route('/logout')
def logout():
	#session needs to be popped off upon logout or browser close to clear 
	session.pop('uid', None)
	flash('You were logged out')
	return redirect(url_for("login"))

@app.route('/wee')
def crash_and_burn():
	return render_template('/wee.html',)

@app.route('/all_movies_by_user')
def list_movies_by_user():
	"""
	- get request
	"""
	uid = session['uid']
	print "uid = ", uid
	movie_list=model.session.query(model.Rating).filter_by(user_id = uid).all()
	return render_template("/all_movies_by_user.html", movie_list = movie_list, uid = uid)

def list_ratings_by_user():
	"""
	- get request
	"""
	pass

def update_rating():
	"""
	- post request
	"""
	pass

def add_rating():
	"""
	- post request
	"""
	pass



if __name__=="__main__":
	app.run(debug=True)
