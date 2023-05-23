#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.26.155.89", "54.157.163.215"]

def do_deploy(archive_path):
    """
    Deploys an archive file to the server

    Args:
        archive_path: path to the archive file to be deployed
        to the server
    Returns:
        True: if successful
        False: if otherwise
    """

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        split_slash = archive_path.split("/")[-1]
        remove_tgz = split_slash.split(".")[0]
        directory = '/data/web_static/releases/'
        run('mkdir -p {}{}'.format(directory, remove_tgz))
        run('tar -xzf /tmp/{0}.tgz -C {1}{0}'.format(remove_tgz, directory))
        run('rm /tmp/{}.tgz'.format(remove_tgz))
        run('mv {0}{1}/web_static/* {0}{1}'.format(directory, remove_tgz))
        run('rm -rf {}{}/web_static'.format(directory, remove_tgz))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}\
                /data/web_static/current'.format(directory, remove_tgz))
        return True
    except Exception as e:
        return False
