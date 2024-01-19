from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')

#this creates a route within the website. You can now go to the http://127.0.0.1:5000 and 
# add /testname to use any name there. That name is then passed to the function and displayed
# in the hello world section
@app.route("/<name>")


def hello(name=None):
    return f"Hello, {escape(name)}!"