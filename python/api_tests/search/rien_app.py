from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Hello World this is home"

@app.route("/calc")
def calc():
	return "testing shit out"


if __name__ == '__main__':
	app.run(debug=True)
