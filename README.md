# Fast Fibonacci
## Is there a difference between rendering a Fibonacci sequence recursively vs with a hash in Python? Go check out the difference.


Along with being a fun little way to show the difference between recursing vs hashing through a Fibonacci sequence, this page is also my first attempt at posting Python code online. While it hasn't gone live yet, I am learning how to do so with Flask. Until then, you can view this program in the terminal.

Quick Notes on viewing in Terminal (MacOS and Python 3)
```
1. Fork this project to your own GH account
2. Clone the repo from your GitHub account
3. Open a terminal on your Mac and navigate to a file where you would like to house this project
4. Type `git clone` and paste the cloned repo
5. cd into the folder with this repo
6. type `python3 fast_fib.py` and hit enter for the hashing function and `python3 slow_fib.py` for the recursive function
7. Protip -- unless you've got a super fast computer, don't go past 45 or so on the slow_fib.py file!
8. Enjoy!
```


My thanks to [Bhavani Ravi's](https://medium.com/bhavaniravi/build-your-1st-python-web-app-with-flask-b039d11f101c) article on Flask, which helped me figure out how to get started.

And to [PzanettiD](https://github.com/PzanettiD/fibonacci-web) for an excellent example of a Fibonacci game on a Flask app.

Quick Installation Fieldnotes for Flask (MacOS)
```
(In the terminal. Assuming you have Python 3.)
$ mkdir yourproject
$ cd yourproject
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```

*For info on how to do this for Python 2, visit the [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-create-env) website*