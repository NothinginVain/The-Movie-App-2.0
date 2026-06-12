from models import db, User, Movie
from flask import jsonify

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        return User.query().all()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()


    def add_movie(self, movie):
        movie_name = movie.name
        movie_check = Movie.query.get(movie_name)
        if movie_check is None:
            return jsonify({'Error':'Movie not found'})

        db.session.add(movie_check)
        db.session.commit()
        return jsonify({'Message':'Movie as been added successfully'})


    def update_movie(self, movie_id, new_title):
        select_movie = Movie.query.get(movie_id)

        if select_movie:
            select_movie.name = new_title
            db.session.commit()

        return select_movie


    def delete_movie(self, movie_id):
        select_movie = Movie.query.get(movie_id)

        if select_movie:
            db.session.delete(select_movie)
            db.session.commit()


        return f'The movie {select_movie.name} was successful deleted'