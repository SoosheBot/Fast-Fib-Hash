# app.py
from flask import Flask, render_template  # import flask and html template

app = Flask(__name__)             # create an app instance

# @app.route("/<name>")                   # at the end point /
# def hello(name):                      # call method hello
#     return "Hello" + " " + name         # which returns "hello and whatever name you put at the end of http://127.0.0.1:5000/"
# if __name__ == "__main__":        # on running python app.py
#     app.run(debug=True)  

@app.route("/")                   
def hello():                     
    return "Hello"
if __name__ == "__main__":        
    app.run(debug=True) 
