from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
	hline = "Hello World!"
	return render_template("index.html",headline=hline)

@app.route("/bye")
def bye():
	hline="Goodbye!"
	return render_template("index.html",headline = hline)