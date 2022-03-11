#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import logging
from logging.handlers import RotatingFileHandler  # 日志回滚
import time


"""
@Time :2022/02/11
@Author :liyinchi
@File :log.py
@Version：1.0
"""


class log:
    def __init__(self):
        pass

    """
        控制台信息保存日志
        :param none
        :return: logger
    """

    def logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
        rHandler = RotatingFileHandler(
            os.getcwd()+"/log/log{}.txt".format(time.strftime("%Y-%y%d %X")), maxBytes=1*1024, backupCount=3)
        rHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rHandler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        logger.addHandler(rHandler)
        logger.addHandler(console)
        return logger
        logger.info("Start print log")
        logger.debug("Do something")
        logger.warning("Something maybe fail.")
