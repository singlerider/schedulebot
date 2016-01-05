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
import sys
reload(sys)
sys.setdefaultencoding("utf8")

channel = config.channel
print channel  # channel connecting to
# we're specifically scraping the Games Done Quick Schedule
SCHEDULE_SITE = "https://gamesdonequick.com/schedule"


class Roboraj(object):

    def __init__(self, config):
        self.config = config  # use config.py as this instance's config
        self.irc = irc_.irc(config)  # use irc.py for socket connections
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


    def run(self):
        n = 0
        WAIT = False
        while True:  # main event loop
            if n < len(self.runs):
                current_run = self.runs[n]
                pattern = "%Y-%m-%dT%H:%M:%SZ"
                t = current_run[0]
                epoch = int(time.mktime(time.strptime(t, pattern)))
                if time.time() > epoch:
                    n += 1
                else:
                    if WAIT == False:
                        WAIT = True
                        print self.runs[n - 1][1]
                        current_run = self.runs[n]
                        new_t = current_run[0]
                        new_epoch = int(time.mktime(time.strptime(t, pattern)))
                        game = unicode(current_run[1])
                        runners = unicode(current_run[2])
                        expected_time = unicode(current_run[3])
                        description = unicode(current_run[4])
                        setup_time = unicode(current_run[5])
                        resp = """Next up: {0}, ran by {1} \
with an expected time of {2}. {3}. Setup time: {4}""".format(
                        game, runners, expected_time, description.rstrip("."), setup_time)
                        print resp
                    while time.time() < new_epoch:
                        pass
                    print "time.time() > new_epoch"
                    print resp
                    self.irc.send_message("#gaming", resp)
                    WAIT = False
                    continue
