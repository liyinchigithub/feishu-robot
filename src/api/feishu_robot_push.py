#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from asyncio.log import logger
import requests
import json
from datetime import datetime as dt
import time
import logging #日志引入
'''
    飞书机器人发送消息
    :param  web_hook 飞书webhook地址
    :param  message_body 发送消息内容
'''
class feishu_robot():
    def __init__(self,web_hook,message_body,payload_message=''):
        self.web_hook=web_hook
        self.message_body=message_body
        self.payload_message=payload_message
    def push(self):
        # 请求头
        header = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        # 请求
        
        try:
            if self.payload_message=='':
               response= requests.post(
                url=self.web_hook, json=self.message_body, headers=header)
            else:
               response= requests.post(
                url=self.web_hook, json=self.message_body, headers=header,data=json.dumps(self.payload_message))
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" %
                        (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                # 返回内容
                opener = response.json()
                logger.info(response.text)
            except json.JSONDecodeError:
                logging.error("服务器响应异常，状态码：%s，响应内容：%s" %
                            (response.status_code, response.text))
                logger.info(u"通知消息发送失败，原因：{}".format(opener))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logging.info('发送结果：%s' % opener)
                return opener
                # 消息发送失败提醒（errcode 不为 0，表示消息发送异常），默认不提醒，开发者可以根据返回的消息发送结果自行判断和处理
        