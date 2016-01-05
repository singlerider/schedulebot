# schedulebot

### This is a Slack chat/irc bot written in Python (2.6 / 2.7).

This is a scraper and notifier for games being played by Games Done Quick (AGDQ and SGDQ)

## Installation

### Virtual Environment

I would recommend running this in a virtual environment to keep your
dependencies in check. If you'd like to do that, run:

`sudo pip install virtualenv`

Followed by:

`virtualenv venv`

This will create an empty virtualenv in your project directory in a folder
called "venv." To enable it, run:

`source venv/bin/activate`

and your console window will be in that virtualenv state. To deactivate, run:

`deactivate`

### Dependencies

To install all dependencies locally (preferably inside your activated
virtualenv), run:

`pip install -r requirements.txt`

### Further Steps

Make a copy of the example config file:

`cp src/config/config_example.py src/config/config.py`

#### Config File

Head into src/config/config.py and enter the channel you'd like to join, your login credentials, and your Slack API Token (descriptions in config file).


### To run:

`./serve.py`
