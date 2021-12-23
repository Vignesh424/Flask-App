from flask import *

app = Flask(__name__)
app.secret_key = "@345^"

@app.route('/hello/')
def index():
    flash("Please enter your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

