# -*- encoding: utf-8 -*-
'''
@create_time: 2020/12/04 14:14:09
@author: lichunyu
'''

import os
from datetime import datetime


from scheduler.app.common.time_calculation.time_difference import time_difference
from scheduler.app.common.tools import is_empty_dir
from scheduler.conf.conf import time_difference_seconds, data_path


def job():
    _dataclean(data_path)



def _dataclean(path_list):
    for path in path_list:
        for root, dirs, files in os.walk(path, topdown=False):
            for file_name in files:
                if time_difference(datetime.fromtimestamp(os.path.getctime(os.path.join(root, file_name)))) > time_difference_seconds:
                    os.remove(os.path.join(root, file_name))

        for root, dirs, files in os.walk(path, topdown=False):
            for dir_name in dirs:
                if time_difference(datetime.fromtimestamp(os.path.getmtime(os.path.join(root, dir_name)))) > time_difference_seconds and \
                                                    is_empty_dir(os.path.join(root, dir_name)):
                    os.rmdir(os.path.join(root, dir_name))
