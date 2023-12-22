#Import the falsk 
from flask import Flask

#Create an instance
app = Flask(__name__)

#Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello,world!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
