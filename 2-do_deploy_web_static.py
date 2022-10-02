#!/usr/bin/python3
'''
    Script distributes an archive to
    web servers through automation
'''
from fabric.api import *
import os

# Servers's addresses
env.hosts = ['35.175.133.237', '44.200.171.3']


def do_deploy(archive_path):
    '''
        Deploy web static content to web server
    '''
    if archive_path is None:
        return False

    start = 'versions'

    try:
        # Get the archive file through the file path
        filename = os.path.relpath(archive_path, start)

        # Upload the archive to /tmp/ dir web server
        put("{}".format(archive_path), "/tmp/{}".format(filename))

        # Cut off both the file extension and dot
        folder = filename.split('.')[0]

        # Create directory on web server
        run("mkdir -p /data/web_static/releases/{}/".format(folder))

        # Uncompress the archive to "folder"
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(filename, folder))

        # Delete archive file from web server
        run("rm /tmp/{}".format(filename))

        # Move content of web_static to "folder"
        run("mv /data/web_static/releases/{0}/web_static/*".format(folder) +
            " /data/web_static/releases/{0}/".format(folder))

        # Delete the content of web_static
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder))

        # Delete symbolic link current on web server
        run("rm -rf /data/web_static/current")

        # Create new link: current and point to new version of code in "folder"
        run("ln -s /data/web_static/releases/{}".format(folder) +
            " /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as err:
        return False
