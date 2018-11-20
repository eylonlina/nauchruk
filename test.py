from flask import Flask, render_template
import db
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/search')
def searchpage():
    return render_template("search.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<username>')
def userpage(username):
    user_data = db.get_user(username)
    return render_template("userpage.html", user=user_data)

app.run(port=5000)
