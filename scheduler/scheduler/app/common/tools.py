# -*- encoding: utf-8 -*-
'''
@create_time: 2020/12/04 15:14:15
@author: lichunyu
'''

import os


def clean_dict(_dict):
    res = {}
    for k, v in _dict.items():
        if v:
            res[k] = v
    return res


def is_empty_dir(path):
    if not os.path.isdir(path):
        raise Exception('path must be dir')
    files = os.listdir(path)
    if not files:
        return True
    else:
        return False