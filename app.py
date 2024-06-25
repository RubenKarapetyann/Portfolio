from flask import Flask
from constants.routes import TEST

app = Flask(__name__)

@app.route(TEST)
def test():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)