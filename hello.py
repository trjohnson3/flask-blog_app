from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
	first_name = "Tom"
	fp = ["pep", " Saus", "pnm", 41]
	return render_template("index.html", 
		first_name=first_name,
		fp=fp)

# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
	return render_template("user.html", name=name)

