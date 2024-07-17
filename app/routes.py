from flask import current_app as app, jsonify

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/echo/<message>')
def echo(message):
    return jsonify({"message": message})
