from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/resume")
def resume():
	return render_template('resume.html')

if __name__ == "__main__":
	app.run()
