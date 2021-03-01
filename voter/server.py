from flask import Flask
from api.api import api_channels
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1200 per day", "50 per hour"]
)

app.register_blueprint(api_channels)


@app.route("/")
def main():
    return "Awesome YouTubers voting system website."


if __name__ == "__main__":
    app.run()
