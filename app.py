# Importing necessary libraries:
from flask import Flask

# Creating a flask app:
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def home():
    return 'Hello World'


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)