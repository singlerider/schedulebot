"""
incrementor for words in a Twitch chat
"""

import lib.irc as irc_
import sys
import datetime
import traceback
import sched
import time
import os
import src.config.config as config
from threading import Thread
from lib.functions_general import *
import src.lib.incoming_data as incoming_data
import src.lib.cron as cron
import requests
from bs4 import BeautifulSoup

channel = config.channel
print channel  # channel connecting to

SCHEDULE_SITE = "https://gamesdonequick.com/schedule"


def cron_job(channel):
    with open("changes.json", "r") as f:  # read changes.json
        changes = json.loads(f.read())  # convert to dict
    with open("changes.json", "w") as f:  # open changes.json
        f.write(json.dumps({}))  # write an empty dict to file
    # {word1: count, word2: count}
    # list comprehension for the chat message return
    word_list = ", ".join([x + " count: " + str(
        changes[x] + 1) for x in changes])
    return word_list


class Roboraj(object):

    def __init__(self, config):
        self.config = config  # use config.py as this instance's config
        self.irc = irc_.irc(config)  # use irc.py for socket connections
        #cron.initialize(
        #    self.irc, self.config.get('channels', {}), (
        #        10, cron_job))
        # asyncronously check for incoming PINGs and send PONGs to server
        incoming_data.initialize(self.irc, self.config.get('channels', {}))
        self.soup = BeautifulSoup(requests.get(SCHEDULE_SITE).content, "html.parser")
        self.table = self.soup.findChildren('tbody', id='runTable')[0]
        self.rows = self.table.findChildren(['th', 'tr'])
        self.runs = []
        for row in self.rows:
            cells = row.findChildren('td')
            result = []
            for cell in cells:
                value = cell.string
                result.append(value)
            if len(result) > 3:
                self.runs.append(result)
        self.irc.send_message("#gaming", str(self.runs[1]))

    def run(self):
        while True:  # main event loop
            pass
