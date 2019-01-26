from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('homepage.html')

@app.route("/resume")
def resume():
	return render_template('resume2.html')

#@app.route('/sentiment_post')
	#make a request to get data from redit
	#run sentiment analyzer using code
	#pass in sentiment ane current post to our html

if __name__ == "__main__":
	app.run()

@app.route("/sent_anl")
def sentiment_analyzer():
	return render_template('sent_anl.html')
