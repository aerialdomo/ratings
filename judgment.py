from flask import Flask, render_template, redirect, url_for, flash, session, request, g
import model
# import urllib
import requests
app = Flask(__name__)

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
	# error = None
	# if request.method == 'POST': # do the login
	# 	if request.form['id'] == model.User.id:
	# 		error = 'Invalid id'
	# 	elif request.form['password'] == model.User.password:
	# 		error = 'Invalid password'
	# 	else:
	# 		session['logged_in'] = True
	# 		flash('You were logged in')
	# 		return redirect('mooovies')
	# #else: # show login form
	# 	#email = request.form['id']
	# 	#password = request.form['password']
	# 	# do we send user to the authentication page?
	return render_template("login.html", )

@app.route('/authenticate', methods=["POST"])	
def authenticate():
	form_password = request.form['password']
	form_uid = request.form['id']
	row = model.session.query(model.User).filter_by(id = form_uid).one()
	if (form_password == row.password) and (int(form_uid) == int(row.id)):
		return render_template('/mooovies.html',)
	else:
		#flash("Please enter a valid id and password.")
		return render_template("/wee.html",)
		# return render_template("/login.html",)

@app.route('/mooovies',)
def list_movies_by_user():
	"""
	- get request
	"""
	uid = 1
	movie_list=model.session.query(model.Rating).filter_by(user_id = uid).all()
	return render_template("/mooovies.html", movie_list = movie_list, uid = uid)

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
