from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

books = {}


def abort_if_book_doesnt_exist(book_id):
    if book_id not in books:
        abort(404, message=f"Book {book_id} doesn't exist.")


parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("author")


class Book(Resource):
    def get(self, book_id):
        abort_if_book_doesnt_exist(book_id)
        return {book_id: books[book_id]}

    def put(self, book_id):
        args = parser.parse_args()
        book = {"name": args["name"], "author": args["author"]}
        books[book_id] = book
        return book, 201

    def delete(self, book_id):
        abort_if_book_doesnt_exist(book_id)
        del books[book_id]
        return "", 204


class Books(Resource):
    def get(self):
        return books


api.add_resource(Book, '/<string:book_id>')
api.add_resource(Books, '/books')

if __name__ == '__main__':
    app.run(debug=True)
