#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import *
from datetime import datetime
from os.path import exists
from os import mkdir


env.hosts = ['18.210.15.214', '54.237.76.221']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the
    function do_deploy"""
    if not exists(archive_path):
        return False
    temp = archive_path.split("/")[-1]
    filename = archive_path
    if temp:
        filename = temp
    tmp_archive = '/tmp/{}'.format(filename)
    result = put(archive_path, tmp_archive)
    if result.failed:
        return False
    targetFile = filename.split(".")[0]
    deploy = '/data/web_static/releases/{}'.format(targetFile)
    result = run("mkdir -p {}".format(deploy))
    if result.failed:
        return False
    result = run("tar -zxvf {} -p -C {}".format(tmp_archive, deploy))
    if result.failed:
        return False
    if result.failed:
        return False
    result = sudo("rm -f {}".format(tmp_archive))
    if result.failed:
        return False
    result = sudo("rm -f /data/web_static/current")
    if result.failed:
        return False
    result = sudo("ln -s {} /data/web_static/current".format(deploy))
    return True
