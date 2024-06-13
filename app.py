# Importing necessary libraries:
from flask import Flask
import numpy as np
import pandas as pd

# Creating a flask app:
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def home():
    return 'Hello World'


if __name__=='__main__':
    app.run()