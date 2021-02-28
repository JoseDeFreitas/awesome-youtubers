from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Working"


if __name__ == "__main__":
    app.run(debug=True)
