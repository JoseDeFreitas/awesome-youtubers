import json
from flask import Blueprint, request, jsonify

with open("data.json", "r", encoding="utf8") as read_data:
    channels = json.load(read_data)

api_channels = Blueprint('api_channels', __name__)


@api_channels.route("/channels/all")
def list_channels():
    """ Lists all channels in the database. """

    return jsonify(channels)


@api_channels.route("/channels")
def get_channel():
    """
    Opens the confirmation form that sends the vote
    to the database corresponding the channel selected.
    """

    if "name" in request.args and "vote" in request.args:
        name = str(request.args["name"])
        vote = str(request.args["vote"])

    if "name" in request.args and "vote" not in request.args:
        return vote
    # else:
    #     return "No name of channel and vote provided."

    if name in channels:
        if vote == "upvote":
            channels[name] += 1
        else:
            channels[name] -= 1

        with open("data.json", "w", encoding="utf8") as write_data:
            json.dump(channels, write_data, indent=4)
        return f"You {vote}d successfully the channel {name}."
    else:
        return "The name specified is not a channel on the list."
