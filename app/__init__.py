import ssl
import os
import config

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Set config from 'config.py'
app.config.from_object(config)

client = MongoClient(app.config['DB_URI'], ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# Create the database if not exists
database = client['placingthebrand']

# Import routes
from app.controllers.test import *