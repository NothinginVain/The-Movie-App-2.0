from flask import Flask
from data_manager import DataManager
from models import db, Movie


app = Flask(__name__)





if __name__ == '__main__':
    app.run(debug=True, port=5002)
