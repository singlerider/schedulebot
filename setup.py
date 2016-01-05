"""
Use setup tools to setup the schedulebot
"""
from setuptools import setup, find_packages

setup(
    name="schedulebot",
    version="0.0.1",
    description="Bot to post new AGDQ runs to Slack",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "schedulebot=schedulebot.serve:main",
        ]
    },
    install_requires=[
        'beautifulsoup4==4.4.1',
        'requests==2.9.1',
        'wheel==0.24.0'
    ],
)
