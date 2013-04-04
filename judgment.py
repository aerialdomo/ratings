from flask import Flask, render_template, redirect, request, url_for
import model
app = Flask(__name__)

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

@app.route("/login", methods = ['GET', 'POST'])
def login():
	"""
	- login.html is a form that contains user name, password
	- info in form is posted to authenticate
	"""
	
	if request.method == 'POST':
		pass
		# do the login.
	else:
		# show login form
		email = request.form['input_email']
		password = request.form['input_password']
		# do we send user to the authentication page?
	return render_template("login.html",)

	
def authenticate():
	"""
	- compares if username, password match records in database
	- returns redirect to a page (list_ratings_by_user?)
	"""
	pass
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
