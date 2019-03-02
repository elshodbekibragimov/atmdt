from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h5>hello {name}!</h5>"
