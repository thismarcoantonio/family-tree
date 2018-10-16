from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

books = [{
  'id': 0,
  'title': 'A Fire Upon the Deep',
  'author': 'Vernor Vinge',
  'first_sentence': 'The coldsleep itself was dreamless.',
  'year_published': '1992'
}, {
  'id': 1,
  'title': 'The Ones Who Walk Away From Omelas',
  'author': 'Ursula K. Le Guin',
  'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
  'published': '1973'
}, {
  'id': 2,
  'title': 'Dhalgren',
  'author': 'Samuel R. Delany',
  'first_sentence': 'to wound the autumnal city.',
  'published': '1975'
}]

@app.route('/books', methods=['GET'])
def home():
  return jsonify(books)

@app.route('/books/<id>')
def book_id(id):
  if not id:
    return jsonify(books)
  results = []

  for book in books:
    print(book['id'] == id)
    if book['id'] == int(id):
      results.append(book)

  return jsonify(results)


app.run()