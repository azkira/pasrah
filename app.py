# app.py
from flask import Flask        # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")
def home():
  return 'Hello, World'

@app.route("/get", methods=['GET'])                
def get():                     
  return {
    "message": "anjing luh bre"
  }

if __name__ == '__main__':
  app.run()