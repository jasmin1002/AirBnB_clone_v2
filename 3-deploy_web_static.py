#!/usr/bin/python3
'''
    Full deployment
'''
from fabric.api import *
import os

# import do_pack and do_deploy module
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

# web servers' addresses
env.hosts = ['35.175.133.237', '44.200.171.3']

def deploy():
    '''
        Script creates and distributes an archive
        to web servers.
    '''
    # Create an archive on web servers
    archive_path = do_pack()

    if os.path.isfile(archive_path) is False:
        return False

    # Distribute an archive to web servers
    return do_deploy(archive_path)
