from schematics.models import Model
from schematics.types import StringType

'''
### PROJECTS COLLECTION SCHEMA ###
Handles the different projects by different users

  _id - handled by mongo
  postcode - project location postcode
  desc - project description
'''

class Projects(Model):
  postcode = StringType(
    max_length=6, 
    required=True
  )
  
  desc = StringType()