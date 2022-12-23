#!/usr/bin/python3
"""The Fabric Tasks"""
from fabric.api import *
from datetime import datetime
from os.path import exists
from os import mkdir


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    hours = today.hour
    minutes = today.minute
    seconds = today.second
    target = "versions/web_static_{}{}{}{}{}{}.tgz".\
             format(year, month, day, hours, minutes, seconds)
    if not exists('versions'):
        mkdir('versions')
    local("tar -zcvf {} web_static".format(target))
