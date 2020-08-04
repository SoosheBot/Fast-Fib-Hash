from flask import Flask, redirect, request, url_for, render_template



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/fast-fib-result', methods=["POST"])
# def fastFibResult():
#     u_input = request.form.get("num")
#     if not u_input:
#         return redirect("/")
#     number = fastFib(int(u_input))
#     return render_template("fast-fib-result.html", fib_num = number, usr_input= u_input)




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)