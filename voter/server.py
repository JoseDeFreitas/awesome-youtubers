from flask import Flask
from api.api import api_channels

app = Flask(__name__)

app.register_blueprint(api_channels)


@app.route("/")
def main():
    return "Working"


if __name__ == "__main__":
    app.run(debug=True)
