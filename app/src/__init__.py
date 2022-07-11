import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
from src import server
def create_app(test_config=None):
    # create and configure the app
    app.run(debug=True, port=5000)


    

