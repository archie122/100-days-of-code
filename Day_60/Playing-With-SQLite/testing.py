from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
db.init_app(app)

# Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# # Create Table
# with app.app_context():
#     db.create_all()
#
# # Entry 1
# entry1 = Book(
#     id=1,
#     title="Harry Potter",
#     author="J. K. Rowling",
#     rating=9.3
# )
#
# # Insert Entry
# with app.app_context():
#     db.session.add(entry1)
#     db.session.commit()

# Read Entry
# with app.app_context():
#     result = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
#     print(result.title)
#     print(result.author)
#     print(result.rating)

# Read all Entries
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#     for book in all_books:
#         print(book.title)
#         print(book.author)
#         print(book.rating)

# Update Entry
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
#     book_to_update.rating = 10
#     db.session.commit()

# Delete Entry
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
#     db.session.delete(book_to_delete)
#     db.session.commit()

