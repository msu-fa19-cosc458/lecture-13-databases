# app.py
import os, flask

app = flask.Flask(__name__)

import models # this needs to be here 

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__': 
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )


