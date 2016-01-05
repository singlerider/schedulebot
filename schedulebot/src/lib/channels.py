import json
import requests

slack_token = ""


def initial_channels(token=None):
    url = "https://slack.com/api/channels.list?token={0}".format(token)
    resp = requests.get(url)
    data = json.loads(resp.content)
    channels = ["#gaming"]
    #channels = ["#" + x["name"] for x in data["channels"]]
    print channels
    return channels
