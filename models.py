from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
# add column to indicate which movies belong to this user, ex: list of movies.ids [ 2, 14, 3 ]

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    poster_url = db.Column(db.String(200))
# add column which users have this specific movie ex: list of user.ids [ 1, 2, 3,]
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class UserMovies(db.Model):
    __tablename__ = 'user_movies'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)