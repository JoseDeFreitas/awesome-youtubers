import threading
from flask import (
    Flask, jsonify,
    make_response, request,
    render_template
)
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# App configuration

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///youtubers.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1200 per day", "50 per hour"]
)

lock = threading.Lock()

# Database model


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    vote = db.Column(db.Integer, default=0, nullable=False)


@app.route("/")
def index():
    """ Main route of the website. """
    return "Awesome YouTubers voting system website."


@app.route("/channels/all")
def list_channels():
    """ Lists all channels in the database. """

    return render_template(
        "all.html",
        channels=Channel.query.order_by(Channel.name).all()
    )


@app.route("/channels/<channel>")
def get_channel(channel):
    """
    If no query specified, prints the name of the
    YouTube channel typed. When a query with the
    name "vote" is given, adds or substracts 1
    from the specified YouTube score.
    """

    if "vote" in request.args:
        vote = str(request.args["vote"])

        if channel in channels:
            # Adds/substracts 1 from the channel.
            if vote == "upvote":
                channels[channel] += 1
            elif vote == "downvote":
                channels[channel] -= 1
            else:
                return "Vote word not recognised."

            # Write to database file.

            return f"You {vote}d successfully the channel {channel}."
        else:
            return "Channel not found on the list."
    else:
        if channel in Channel.query.order_by(Channel.name).all():
            return "Channel: " + channel
        else:
            return "Channel not found on the list."


@app.route("/channels/<channel>/image.svg")
def img_channel(channel):
    """ Returns the YouTube score in a svg image. """

    if channel in Channel.query.order_by(Channel.name).all():
        svg_image = f"""
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                width="52px" height="22px" viewBox="0 0 52 22" fill="none">
                <style>
                    .text {{
                        font-family: "Segoe UI", Ubuntu, Sans-Serif;
                        font-weight: bold;
                    }}
                    </style>
                    <rect x="0.5" y="0.5" height="99%" width="51" fill="none"/>
                    <g>
                        <text x="5" y="15" fill="#00b4f0" class="text">
                            {channels[channel]}
                        </text>
                    </g>
                </svg>
                """

        response = make_response(svg_image)
        response.headers.set('Content-Type', 'image/svg+xml')
        return response
    else:
        return "Channel not found on the list"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
