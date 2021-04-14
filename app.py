import flask
from flask import request
import pandas as pd


app = flask.Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    arg = request.args['arg']
    return 'Hello World'