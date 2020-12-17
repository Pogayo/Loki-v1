# Loki
---
- Machine Translation project for English - Acholi.
- Find [here the link]()to the application.
- You can check out the notebooks used for training the models in the notebooks folder

### Modules used
---
| Module Name    | Usage in Application |
|----------------|----------------------|
|Flask           |Web Framework to create Application|
|Flask-Login     | User Session Management in Flask|
|Flask-SQLAlchemy|Adding support of SQLAlchemy into application|
|Flask-WTF       | provide the interactive user interface for the user |
|SQLAlchemy      |Provide ORM and  full power and flexibility of SQL |
|Werkzeug        |For hashing and checking password|
|WTForms         |flexible forms validation and rendering|

### Installation
---
- Install all the dependancies using requirements.txt file...
- ```pip install requirements.txt```

### Running
---
##### Setup on Windows
- setting flask application in Windows
- ```set FLASK_APP=app.py```
- ```set FLASK_DEBUG=1```

##### Setup on Unix
- setting flask application in Unix
- ```export FLASK_APP=app.py```
- ```export FLASK_DEBUG=1```

#### Run Application
- After setting flask application, To run application use below command
- ```flask run --port=8080```
- ```--port``` is optional
