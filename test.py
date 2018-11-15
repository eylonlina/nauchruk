from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

app.run(port=5000)
