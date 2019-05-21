# Placing the Brand Master

## How to run
* Create a `config.py` file in the following format

`DEBUG = True`  
`PORT = 5000`  
`HOST = "0.0.0.0"`  
`DB_URI = "Database URL [Ask Toby for details]"`  

* Create a new virtual enviroment for Python `python3 -m venv mastervenv`
* Run virtual env `source mastervenv/bin/activate`
* Install everything `pip install -r requirements.txt`
* Run the server `python run.py`

NOTE: When you install a new package you need to run `pip freeze > requirements.txt`

## Project Structure
`- app/` - The main python application  
&ensp;&ensp;  `- controllers/` - App controller  
`- data/` - Data handling (retrieval)  
`- doc/` - Documentation  
`- models` - Database model schemas  
`- ml/` - Machine Learning (mostly models)  
`- lib/` - Utility functions  
`- prepross/` - Data preprocessing  
`- reports/` - ML Reports  