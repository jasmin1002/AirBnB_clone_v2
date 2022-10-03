#!/usr/bin/python3
'''
    Full deployment
'''
from fabric.api import *
import os
from datetime import datetime

# web servers' addresses
env.hosts = ['35.175.133.237', '44.200.171.3']


def do_pack():
    '''
        Generate a compressed archive file
    '''
    dt = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create an archive filename by date and time
    f_archive = 'web_static_' + dt + '.tgz'
    directory = 'versions'

    # Create directory if it doesn't exist
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)

    # Process feedback
    msg = 'Packing web_static to {}/{}'.format(directory, f_archive)
    print(msg)

    result = local(
        "tar -cvzf {}/{} web_static".format(directory, f_archive),
        capture=False
    )

    if result.succeeded:
        # Archive file path
        path = '{}/{}'.format(directory, f_archive)

        # Archive file size
        f_size = os.path.getsize(path)

        # Process feedback
        msg = 'web_static packed: {} -> {}Bytes'.format(
            path,
            f_size
        )

        print(msg)
        return path
    else:
        return None


def do_deploy(archive_path):
    '''
        Distribute archive file to all hosts
        (web servers)
    '''
    if os.path.exists(archive_path) is False:
        return False

    try:
        filename = os.path.relpath(archive_path, 'versions')
        put(archive_path, "/tmp/{}".format(filename))
        folder = filename.split('.')[0]

        ws_path = '/data/web_static/releases/{}'.format(folder)

        run("mkdir -p {}".format(ws_path))
        run("tar -xzf /tmp/{} -C {}/".format(filename, ws_path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(ws_path))
        run("rm -rf {}/web_static".format(ws_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web-static/current".format(ws_path))

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    '''
        Script creates and distributes an archive
        to web servers.
    '''
    # Create an archive on web servers
    path = do_pack()

    if os.path.exists(path) is False:
        return False

    # Distribute an archive to web servers
    return do_deploy(path)
