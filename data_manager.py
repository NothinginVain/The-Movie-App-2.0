from models import db, User, Movie, UserMovies


class DataManager:
    """
    Manage database operations for users and movies.

    Provides methods for creating, retrieving, updating,
    and deleting records.
    """


    def create_user(self, name):
        """
        Create and save a new user.

        Args:
            name (str): User name.

        Returns:
            bool: True if the user was created successfully.
        """
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return True


    def get_users(self):
        """
        Retrieve all users.

        Returns:
            list: List of User objects.
        """
        return User.query.all()


    def get_user(self, user_id):
        """
        Retrieve a user by ID.

        Args:
            user_id (int): User ID.

        Returns:
            User | None: Matching user or None.
        """
        return User.query.get(user_id)

    def get_user_by_name(self, name):
        """
        Retrieve a user by name.

        Args:
            name (str): User name.

        Returns:
            User | None: Matching user or None.
        """
        return User.query.filter_by(name=name).first()

    def get_movies(self, user_id):
        """
        Retrieve all movies belonging to a user.

        Args:
            user_id (int): User ID.

        Returns:
            list: List of Movie objects.
        """
        return Movie.query.filter_by(user_id=user_id).all()

    def get_movie_by_name(self, movie_name):
        """
        Retrieve a movie by its name.

        Args:
            movie_name (str): Movie title.

        Returns:
            Movie | None: Matching movie or None.
        """
        return Movie.query.filter_by(name=movie_name).first()

    def movie_exists_for_user(self, user_id, movie_name):
        """
        Check whether a movie already exists for a user.

        Args:
            user_id (int): User ID.
            movie_name (str): Movie title.

        Returns:
            Movie | None: Matching movie or None.
        """
        return Movie.query.filter_by(
            user_id=user_id,
            name=movie_name
        ).first()

    def add_movie(self, movie):
        """
        Save a movie to the database.

        Args:
            movie (Movie): Movie object to save.

        Returns:
            bool: True if saved successfully.
        """
        db.session.add(movie)
        db.session.commit()
        return True


    def update_movie(self, movie_id, new_title):
        """
        Update a movie title.

        Args:
            movie_id (int): Movie ID.
            new_title (str): New movie title.

        Returns:
            Movie | None: Updated movie or None if not found.
        """
        select_movie = Movie.query.get(movie_id)

        if select_movie:
            select_movie.name = new_title
            db.session.commit()

        return select_movie


    def delete_movie(self, movie_id):
        """
        Delete a movie from the database.

        Args:
            movie_id (int): Movie ID.

        Returns:
            bool: True if deleted, otherwise False.
        """
        select_movie = Movie.query.get(movie_id)

        if select_movie:
            db.session.delete(select_movie)
            db.session.commit()
            return True
        else:
            return False
