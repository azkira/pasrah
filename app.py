# app.py
from flask import Flask        # import flask
app = Flask(__name__)             # create an app instance

@app.route("/get", methods=['GET'])                   # at the end point /
def home():                      # call method hello
  return {
    "message": "anjing luh bre"
  }

if __name__ == '__main__':
  app.run()