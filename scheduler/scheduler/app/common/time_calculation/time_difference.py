# -*- encoding: utf-8 -*-
'''
@create_time: 2020/12/04 14:58:44
@author: lichunyu
'''

from datetime import datetime

def time_difference(target=None, source=None, return_to='seconds'):
    if source is None:
        source = datetime.now()
    if return_to == 'seconds':
        return (source - target).seconds