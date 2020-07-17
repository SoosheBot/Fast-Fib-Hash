from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world'

# @app.route('/fibo')
# def fibo():
#     return 'fibo'


if __name__ == "__main__":
    app.run(threaded=True, port=6000)