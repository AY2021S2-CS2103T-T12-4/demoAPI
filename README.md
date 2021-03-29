## demoAPI
solution adapted from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

## steps:
dependancies:
* pip install flask

start local server by running: `python3 api.py`

example APIs to try out: 
home page: 
  * http://127.0.0.1:5000/

get all books: 
  * http://127.0.0.1:5000/api/v1/resources/books/all

get a particular book, from 0 to 2:
  * http://127.0.0.1:5000/api/v1/resources/books?id=0
  * http://127.0.0.1:5000/api/v1/resources/books?id=1
  * http://127.0.0.1:5000/api/v1/resources/books?id=2

test time out
  * http://127.0.0.1:5000/timeout
