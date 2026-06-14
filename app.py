from flask import Flask, render_template, request, redirect, url_for, flash
from data_manager import DataManager
from models import db, Movie
import os
from movie_api import fetch_movie_data


app = Flask(__name__)

"""
Flask application for managing users and their movie collections.

Provides functionality to create users, add movies from an external API,
update movie information, and delete movies.
"""

DEFAULT_IMG_POSTER = 'https://placehold.co/380x562?text=No+Poster'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class

@app.route('/')
def index():
    """
        Display the home page with all registered users.
    """
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.

    Validates the submitted username and prevents duplicates.
    """
    new_user = request.form.get('add_user', '').strip()

    if not new_user:
        flash('User name cannot be empty')
        return redirect(url_for('index'))

    existing_user = data_manager.get_user_by_name(new_user)
    if existing_user:
        flash('User already exists')
        return redirect(url_for('index'))

    save_data = data_manager.create_user(new_user)

    if save_data is True:
        flash('User created with Success')

    return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def user_movies(user_id):
    """
    Display all movies belonging to a user.

    Args:
        user_id (int): ID of the user.
    """
    movies = data_manager.get_movies(user_id)
    user = data_manager.get_user(user_id)
    if user is None:
        flash('User not found')
        return redirect(url_for('index'))

    return render_template('movies.html', movies=movies, user=user)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """
    Add a movie to a user's collection.

    Retrieves movie details from the external API and
    stores them in the database.

    Args:
        user_id (int): ID of the user.
    """
    check_movie = request.form.get('new_movie','').strip()

    if not check_movie:
        flash('Movie title cannot be empty')
        return redirect(url_for('user_movies', user_id=user_id))

    existing_movie = data_manager.movie_exists_for_user(user_id,check_movie)

    if existing_movie:
        flash('Movie already exists')
        return redirect(url_for('user_movies', user_id=user_id))
    # if data_manager.get_movie_by_name(check_movie):
    #     data_manager.add_movie_relation()
    #     going to add user id, and movie id to the user_movie table,
    #if not available in database need to do 3 actions,
    #n1- fetch the movie info from api, n2-add the movies to movies table, n3-add movie id and user id to the third table

    movie_data = fetch_movie_data(check_movie)

    if movie_data is None:
        flash("Error connecting to API, try later.")
        return redirect(url_for('user_movies', user_id=user_id))

    if movie_data.get('Response') == 'False':
        flash('Movie not found.')
        return redirect(url_for('user_movies', user_id=user_id))


    title = movie_data.get('Title', 'N/A')
    year = movie_data.get('Year', 'N/A')
    director = movie_data.get('Director', 'N/A')
    poster = movie_data.get('Poster', 'N/A')
    if poster == "N/A":
        poster = DEFAULT_IMG_POSTER

    new_movie = Movie(name=title, director=director, year=year, poster_url=poster, user_id=user_id)
    save_data = data_manager.add_movie(new_movie)

    if save_data is True:
        flash('Movie add with Success')

    return redirect(url_for('user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """
     Update a movie's title.

     Args:
         user_id (int): ID of the user.
         movie_id (int): ID of the movie.
     """
    new_title = request.form.get('new_title', '').strip()
    if not new_title:
        flash('Movie title can not be empty')
        return redirect(url_for('user_movies', user_id=user_id))

    movie = data_manager.update_movie(movie_id, new_title)

    if movie is None:
        flash('Movie not found')
        return redirect(url_for('user_movies', user_id=user_id))

    flash('Movie updated with Success')
    return redirect(url_for('user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """
        Delete a movie from a user's collection.

        Args:
            user_id (int): ID of the user.
            movie_id (int): ID of the movie.
    """
    deleted = data_manager.delete_movie(movie_id)

    if deleted is False:
        flash('Movie not found')
        return redirect(url_for('user_movies', user_id=user_id))
    else:
        flash(f'The Movie was deleted with Success')
        return redirect(url_for('user_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    """
      Render the custom 404 error page.

      Args:
          e: Exception raised by Flask.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Render the custom 500 error page.

    Args:
        e: Exception raised by Flask.
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5002)
