from flask import request, jsonify
from flask_jwt_extended import jwt_required
from .models import Book, db

def init_routes(app):
    @app.route('/')
    def index():
        return 'Welcome to the Books Service!'

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books]), 200

    @app.route('/books', methods=['POST'])
    @jwt_required()
    def add_book():
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(message="Book added"), 201

    @app.route('/books/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_book(id):
        data = request.get_json()
        book = Book.query.get(id)
        if book:
            book.title = data['title']
            book.author = data['author']
            db.session.commit()
            return jsonify(message="Book updated"), 200
        else:
            return jsonify(message="Book not found"), 404

    @app.route('/books/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_book(id):
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify(message="Book deleted"), 200
        else:
            return jsonify(message="Book not found"), 404
