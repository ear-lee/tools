# -*- encoding: utf-8 -*-
'''
@create_time: 2020/12/04 14:14:09
@author: lichunyu
'''

import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from scheduler.app.common.logger import get_logger
from scheduler.app.common.tools import clean_dict
from scheduler.conf.conf import dataclean_interval
from scheduler.app.job import job


_logger = get_logger(autopath=True)


def test():
    # _logger.info('test')
    a = 1

def scheduler_server():
    _scheduler = BlockingScheduler()
    interval = clean_dict(dataclean_interval)
    _scheduler.add_job(test, 'interval', **interval)
    _scheduler.start()


