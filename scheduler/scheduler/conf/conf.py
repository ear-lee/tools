# -*- encoding: utf-8 -*-
'''
@create_time: 2020/12/04 14:16:53
@author: lichunyu
'''

from datetime import datetime

root_path = '/'  # log 限制地址
time_difference_seconds = 60*0

dataclean_interval = {
    'weeks': '',  # type: [int] - number of weeks to wait
    'days': '',  # type: [int] - number of days to wait
    'hours': '',  # type: [int] - number of hours to wait
    'minutes': '',  # type: [int] - number of minutes to wait
    'seconds': 30,  # type [int] - number of seconds to wait
    'start_date': '',  # type [datetime|str] - starting point for the interval calculation
    'end_date': '',  # type [datetime|str] - latest possible date/time to trigger on
    'timezone': ''  # type [datetime.tzinfo|str] - time zone to use for the date/time calculations
}


# 内部
data_path = ['/Users/lichunyu/Desktop/datagrand/scheduler/scheduler/data']