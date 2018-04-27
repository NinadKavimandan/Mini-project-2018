from flask import Flask, current_app, Response
from flask_cors import CORS
import json
import modules

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
	return current_app.send_static_file('index.html')
	pass

@app.route("/extract/<text>")
def getSum(text):
	data = {}
	data['id'] = 1
	data['summary'] = modules.getSumExtractive(text)
	js = json.dumps(data)
	result = Response(js, status=200, mimetype='application/json')
	return result

if __name__ == "__main__":
	app.run(host = '127.0.0.1', port = 5000)