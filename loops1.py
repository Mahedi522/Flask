from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	names=("rahim","karim","abdul","jabdul")
	return render_template("loops1.html",names=names)