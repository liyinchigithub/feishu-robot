#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import hashlib
import base64
import hmac

"""
    @Time :2022/02/11
    @Author :liyinchi
    @File :main.py
    @Ddescription: 飞书机器人签名
"""
class sign:
  def __init__(self,timestamp, secret):
        self.timestamp=timestamp
        self.secret=secret
  
  def gen_sign(self):
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(self.timestamp, self.secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')
    print("timestamp",self.timestamp)
    print("sign",sign)
    return sign