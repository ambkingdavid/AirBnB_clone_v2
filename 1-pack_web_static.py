#!/usr/bin/python3
"""Fabfile to generates a .tgz archive from the contents of web_static."""
import os.path
from datetime import datetime
from fabric.api import local, lcd

def do_pack():
    """Generates a .tgz archive from the
       contents of the web_static folder
    """
    try:
        local("sudo mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(current_time)
        with lcd("web_static"):
            local("tar -cvzf {} .".format(file_path))
        return file_path
    except:
        return None
