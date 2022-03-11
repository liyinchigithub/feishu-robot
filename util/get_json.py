#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import time
import datetime
import json
from bunch import Bunch

"""
    @Time :2022/02/11
    @Author :liyinchi
    @File :jira_get.py
    @Version：1.0
    @Ddescription: 配置读取函数提供的功能和扩展，如下：配置文件是JSON格式；配置文件转换为配置类和配置字典
"""
class config():
    def __init__(self,json_file):
        self.json_file=json_file
    # 读取json配置文件内容
    def get_config_from_json(self):
        """
        将配置文件转换为配置类
        :param json_file: json文件
        :return: 配置信息
        """
        with open(self.json_file, 'r') as f:
            config_dict = json.load(f)  # 配置字典
        config = Bunch(config_dict)  # 将配置字典转换为类
        return config
