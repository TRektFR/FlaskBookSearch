from flask import Flask, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

books = json.load(open("/home/ubuntu/Bureau/books.json"))

@app.route('/api/books', methods=['GET'])
def Books():
    return jsonify(books), 200


@app.route('/api/search/id/<isbn>', methods=['GET'])
def bookIsbn(isbn):
    for book in books:
        if isbn == book['isbn']:
            return jsonify(book), 200
    return print("we can't find your book"), 404

@app.route('/api/search/title/<title>', methods=['GET'])
def bookTitle(title):
    for book in books:
        if title == book['title']:
            return jsonify(book), 200
    return print("we can't find your book"), 404
