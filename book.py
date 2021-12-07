from flask import Flask, request, render_template, redirect, url_for, jsonify
import json

app = Flask(__name__)

books = json.load(open("Data/books.json"))

@app.route('/api/books', methods=['GET'])
def Books():
    return jsonify("200"),200


@app.route('/api/search/id/<isbn>', methods=['GET'])
def bookIsbn(isbn):
    book = None
    for book in books:
        if isbn == book['isbn']:
            return render_template("book_template.html", book=book)
    return jsonify("book"),404

@app.route('/api/search/title/<title>', methods=['GET'])
def bookTitle(title):
    book = None
    for book in books:
        if title == book['title']:
            return jsonify(book), 200
    return jsonify(None), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
# this is a commentary to try volumes it doesn't work
