<<<<<<< HEAD
from flask import current_app as app, jsonify

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/echo/<message>')
def echo(message):
    return jsonify({"message": message})
=======
from flask import current_app as app, jsonify

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/echo/<message>')
def echo(message):
    return jsonify({"message": message})
>>>>>>> 383a55dab16c3c6b2eb3e0ff1b362f6ccf4b9ca8
