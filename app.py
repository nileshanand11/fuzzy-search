#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from main.fuzzy_search import get_suggetions
import json

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify("Coming soon")

@app.route('/search', methods=['GET'])
def get_words():
	word = request.args.get('word')
	response = get_suggetions(word)
	return json.dumps(response)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)\
