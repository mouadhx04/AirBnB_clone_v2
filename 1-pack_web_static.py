#!/usr/bin/python3
""" use fabric to generate a .tgz archive from the contents"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """generate .tgz file from web_static folder"""
    if not os.path.exists('versions'):
        local('mkdir versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    str_ = 'tar -cvzf versions/web_static_'
    str_ += time
    str_ += '.tgz web_static/'
    try:
        local(str_)
    except Exception as e:
        return None
    return 'versions/web_static_{time}.tgz'.format(time)
