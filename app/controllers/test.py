from flask import jsonify

from app import app, database

''' Test connection route '''
@app.route('/', methods=['GET'])
def connectionTest():
  return jsonify({
    'message': 'connection success'
  })