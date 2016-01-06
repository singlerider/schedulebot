#!/usr/bin/env python2.7

from schedulebot.src.bot import Roboraj
from schedulebot.src.config.config import config


def main():
    bot = Roboraj(config).run()

if __name__ == "__main__":
    main()
