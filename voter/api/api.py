import json
from flask import Blueprint, request, jsonify

with open("data.json", "r") as read_data:
    channels = json.load(read_data)

api_channels = Blueprint('api_channels', __name__)


@api_channels.route("/channels/all")
def list_channels():
    """ Lists all channels in the database. """

    return jsonify(channels)


@api_channels.route("/channels", methods=["GET", "POST"])
def get_channel():
    """
    Opens the confirmation form that sends the vote
    to the database corresponding the channel selected.
    """

    if "name" in request.args:
        name = str(request.args["name"])
    else:
        return "No name of channel provided."

    if name in channels:
        return "Good!"
    else:
        return "The name specified is not a channel on the list."
