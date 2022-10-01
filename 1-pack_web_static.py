#!/usr/bin/python3
'''
    Script to generate a tgz archive file
'''
from datetime import datetime
import os
from fabric.api import *

def do_pack():
    # Generate datetime object
    #today = datetime.now()

    # Convert datetime obj to str
    #today = today.strftime("%Y%m%d%H%M%S")

    path = './versions'
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)


    local("tar -cvzf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz web_static")
    #print(type(today))
    #print("Today's date: {}".format(today))

