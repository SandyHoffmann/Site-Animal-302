# imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify, request
from flask_cors import CORS
import os 
import json
from model import Zoologico
from model import Cuidador
from model import Animal
app = Flask(__name__) 
CORS(app)
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'animal.db') 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+arquivobd 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

