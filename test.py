from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<username>')
def userpage(username):
    return render_template("userpage.html", username=username)

app.run(port=5000)
