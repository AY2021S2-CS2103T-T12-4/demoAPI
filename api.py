import flask
from flask import request, jsonify
import time

# solution adapted from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The cold sleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is my very first website</h1>
<p>You can make API calls to me! I contain a list of books!</p>'''

# A route to return all supported request methods
@app.route('/api/v1/options', methods=['OPTIONS'])
def options():
    return "Allowed request method: \"GET\""

@app.route('/timeout', methods=['GET'])
def timeout():
    time.sleep(60)
    return '''<h1>You waited for 60 seconds! Are you timed out?</h1>
<p>I will wait 60 seconds before sending this to you</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


# example: http://127.0.0.1:5000/api/v1/resources/books?id=0 127.0.0.1:5000/api/v1/resources/books?id=1
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()

'''
start local server by running:
python3 api.py

example APIs to try out: 
home page: http://127.0.0.1:5000/

get all books:
http://127.0.0.1:5000/api/v1/resources/books/all

get a particular book, from 0 to 2:
http://127.0.0.1:5000/api/v1/resources/books?id=0
http://127.0.0.1:5000/api/v1/resources/books?id=1
http://127.0.0.1:5000/api/v1/resources/books?id=2

test time out
http://127.0.0.1:5000/timeout
'''
