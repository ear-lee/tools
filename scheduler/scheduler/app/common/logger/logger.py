# -*- encoding: utf-8 -*-
'''
@create_time: 2020/04/26 18:42:58
@author: lichunyu
'''
import logging
import os
import traceback

# root_path = '/Users/lichunyu/Desktop/'  # 从setting中加载
from scheduler.conf.conf import root_path


def _get_logger(level='info', path='', log_name='', file_name='log', autopath=False):
    """
    @param level: 设置log的level，不区分大小写
    @param path: 指定log的存放地址
    @param log_name: 指定log的文件名，不指定默认为root.log，不以.log结尾会自动补全.log
    @param file_name: 指定存放log的文件夹名称，默认为log，尽量不要修改
    @param autopath: 自动寻找log位置，即从调用文件的路径开始(包含同层)向上至项目根目录，找到最近的log文件夹
    """
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d]\
 %(levelname)s %(message)s')
    logger_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    if level.lower() not in logger_level.keys():
        raise Exception('the param named level must be in [debug, info, warning, error, critical]')
    logger.setLevel(logger_level[level.lower()])
    log_path = _check_file(path=path, log_name=log_name, file_name=file_name, autopath=autopath)
    if not log_path:
        raise Exception('please make sure the file named log is in your directory,\
 otherwise give the param named path')
    fh = logging.FileHandler(log_path)
    ch = logging.StreamHandler()
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def _check_file(path='', log_name='', file_name='log', autopath=False):
    """
    @attention: 返回log文件路径及文件名 ->string
    @param parmas: 参数同上(function: _get_logger)
    """
    if log_name:
        if log_name[-4:] != '.log':
            log_name = log_name + '.log'
    else:
        log_name = 'root.log'
    if path:
        file_path = os.path.abspath(os.path.dirname(path))
    elif autopath is True:
        current_filename = traceback.extract_stack()[-3].filename
        file_path = os.path.abspath(os.path.dirname(current_filename))
        while True:
            if file_path == os.path.abspath(os.path.dirname(root_path)):
                file_path = ''
                break
            layer_dirs_list = [dirs for root, dirs, files in os.walk(file_path)][0]
            if 'log' in layer_dirs_list:
                break
            file_path = os.path.abspath(os.path.dirname(file_path))
        if not file_path:
            return ''
        return file_path + '/log/' + log_name
    else:
        current_filename = traceback.extract_stack()[-3].filename
        # file_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.abspath(os.path.dirname(current_filename))
    dirs_list = [dirs for root, dirs, files in os.walk(file_path)][0]
    if file_name in dirs_list:
        return file_path + '/log/' + log_name
    return ''
