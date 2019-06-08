from flask import jsonify, abort, request, json, Response
from schematics.exceptions import ValidationError

from app import app, database
from app.models.projects import *

def checkRequest(r):
  if not r.json:
    abort(400)

''' Create a new project [ POST ] '''
@app.route('/project/create', methods=['POST'])
def projectCreate():
  checkRequest(request)
  data = request.json

  # Create new Projects model
  newProject = Projects()
  newProject.postcode = data['postcode']
  newProject.desc = data['desc']
  try:
    newProject.validate()

    # Now store in database
    projectsCollection = database.projects
    projectData = newProject.to_native()
    inserted = projectsCollection.insert_one(projectData).inserted_id

    return jsonify({
      'success': True,
      'id': inserted
    })
  except Exception as error:
    response = Response(json.dumps({'error': str(error)}), 400, mimetype='application/json')
    return response