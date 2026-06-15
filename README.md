# MoviWeb App 🎬

MoviWeb App is a Flask web application that allows users to manage their favorite movies. Users can create profiles, add movies to their personal collection, update movie titles, and remove movies from their lists.

Movie information is automatically retrieved from the OMDb API, including the title, release year, director, and poster image.

---

## Features

* Create and manage users
* Add movies to a user's collection
* Retrieve movie information from the OMDb API
* Display movie posters
* Update movie titles
* Delete movies from a collection
* Flash messages for user feedback
* Custom 404 and 500 error pages
* Responsive and clean user interface

---

## Technologies Used

* Python 3
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* Jinja2 Templates
* OMDb API

---

## Project Structure

```text
The-Movie-App-2.0/
│
├── app.py
├── data_manager.py
├── models.py
├── movie_api.py
│
├── data/
│   └── movies.db
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── movies.html
│   ├── 404.html
│   └── 500.html
│
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd The-Movie-App-2.0
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
OMDB_API_KEY=your_omdb_api_key
```

Replace the values with your own credentials.

---

## Database Setup

Initialize the SQLite database before running the application.

Example:

```python
from app import app
from models import db

with app.app_context():
    db.create_all()
```

---

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5002
```

---

## Usage

### Home Page

* View all users
* Create a new user

### Movie Collection

* View a user's favorite movies
* Add a movie by title
* Automatically retrieve movie information from OMDb
* Update movie titles
* Delete movies

---

## Error Handling

The application includes:

* Input validation
* Duplicate user prevention
* Duplicate movie prevention
* OMDb API error handling
* Custom 404 page
* Custom 500 page

---

## Future Improvements

* Many-to-many relationship between users and movies
* Movie ratings
* Search and filtering
* User authentication
* Pagination
* Improved UI animations and styling

---

## Author

José Miguel Ramos

Built as part of a Flask and SQLAlchemy learning project.
