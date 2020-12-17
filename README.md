# Loki
---
- Machine Translation project for English - Acholi.
- Find [here the link](https://loki-mt.herokuapp.com/)to the application.
- You can check out the notebooks used for training the models in the notebooks folder
- The models are found in models folder and tokenizers in the tokenizers folder
- HuggingFace Models and tokenizers were used to initialize the weights. Find them [here](https://huggingface.co/Helsinki-NLP/opus-mt-luo-en#)
- This is a Flask application

### Modules used
---
| Module Name    | Usage in Application |
|----------------|----------------------|
|Torch          |DL Framework|
|Transformers   | Models and Tokenizers|


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
