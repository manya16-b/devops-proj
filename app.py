from flask import Flask 
app=Flask(__name__)
@app.route("/info")
def info():
	return "hey i am manya"
@app.route("/phone")
def phone():
	return "8005600073"
app.run(host="0.0.0.0")