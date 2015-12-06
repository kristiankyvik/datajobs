from flask import Flask
from flask import render_template

app = Flask(__name__)

app.debug = True

@app.route('/')

def index():
	data = { "count": 3}
	return render_template("index.html", data=data )

if __name__ == '__main__':
    app.run()