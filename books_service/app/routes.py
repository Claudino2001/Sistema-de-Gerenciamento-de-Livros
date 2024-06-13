from flask import request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, decode_token, get_jwt_identity
from .models import Book, db

def init_routes(app):
    @app.route('/')
    def index():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                return render_template('index.html', token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/books', methods=['GET'])
    def get_books():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                books = Book.query.all()
                return render_template('books.html', books=books, token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                if request.method == 'POST':
                    data = request.form
                    new_book = Book(title=data['title'], author=data['author'])
                    db.session.add(new_book)
                    db.session.commit()
                    return redirect(url_for('get_books', token=token))
                return render_template('add_book.html', token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
    def edit_book(id):
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                book = Book.query.get(id)
                if request.method == 'POST':
                    data = request.form
                    book.title = data['title']
                    book.author = data['author']
                    db.session.commit()
                    return redirect(url_for('get_books', token=token))
                return render_template('edit_book.html', book=book, token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/delete_book/<int:id>', methods=['POST'])
    def delete_book(id):
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                book = Book.query.get(id)
                db.session.delete(book)
                db.session.commit()
                return redirect(url_for('get_books', token=token))
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400
