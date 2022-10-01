#!/usr/bin/python3

import os
from datetime import datetime
from fabric.api import *


def do_pack():
    '''
        Script to generate a compressed archive file
    '''
    today = datetime.now()
    today = today.strftime("%Y%m%d%H%M%S")

    filename = 'web_static_' + today + '.tgz'
    path = './versions'
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)

    msg = 'Packing web_static to versions/{}'.format(filename)
    print(msg)
    local("tar -cvzf versions/{} web_static".format(filename))
