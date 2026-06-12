from models import db, User, Movie, UserMovies


class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()


    def get_users(self):
        return User.query.all()

    def get_user(self, user_id):
        return User.query.get(user_id)

    def get_user_by_name(self, name):
        return User.query.filter_by(name=name).first()


    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()


    def get_movie_by_name(self, movie_name):
        return Movie.query.get(name=movie_name)


    def movie_exists_for_user(self, user_id, movie_name):
        return Movie.query.filter_by(user_id=user_id, name=movie_name).first()

    def add_movie(self, movie):
        # movie_name = movie.name
        # movie_check = Movie.query.get(movie_name)
        # if movie_check is None:
        #     return jsonify({'Error':'Movie not found'})

        db.session.add(movie)
        db.session.commit()
        # return jsonify({'Message':'Movie as been added successfully'})

    def add_movie_relation(self, user_id):
        movie_id = Movie.query.get(user_id=user_id)
        user_movies_raw = UserMovies(user_id=user_id, movie_id=movie_id)
        db.session.add(user_movies_raw)
        db.session.commit()


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


        # return f'The movie {select_movie.name} was successful deleted'