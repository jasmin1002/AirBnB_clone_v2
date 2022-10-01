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
    result = local(
        "tar -cvzf versions/{} web_static".format(filename),
        capture=False
    )

    if (result.succeeded):
        # Archive file path
        path = '{}/{}'.format(path, filename)

        # Current working directory
        start = os.getcwd()

        # Archive relative file path from working directory
        relative_path = os.path.relpath(path, start)

        # Archive file size
        file_size = os.path.getsize(relative_path)

        msg = 'web_static packed: {} -> {}Bytes'.\
            format(relative_path, file_size)
        print(msg)
        return relative_path 
    else:
        return None
