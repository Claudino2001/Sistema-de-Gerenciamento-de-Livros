from flask import request, jsonify
from flask_jwt_extended import jwt_required
from . import app
import sqlite3

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    title = request.json.get('title')
    author = request.json.get('author')
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Book added"}), 201

@app.route('/books/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    title = request.json.get('title')
    author = request.json.get('author')
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, id))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Book updated"})

@app.route('/books/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Book deleted"})
