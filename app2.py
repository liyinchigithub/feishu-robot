#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import os
from util.get_json import config
from asyncio.log import logger
import time
from src.api.log import log  # 封装日志引入
from src.api.feishu_robot_push import feishu_robot  # 飞书机器人引入
from src.api.feishu_sign import sign  # 飞书签名
import random
from pytz import timezone

# 日志实例化
logger = log().logger()
# 读取配置文件
Config = config("{}/config/config.json".format(os.getcwd())).get_config_from_json()

def cleaning_lottery_job():
    cleaning_cfg = Config.get("cleaning_lottery", {})
    members = cleaning_cfg.get("members", [])
    tasks = cleaning_cfg.get("tasks", [])

    # 新结构：members 是字典列表
    male_members = [m["name"] for m in members if m["gender"] == "男"]
    female_members = [m["name"] for m in members if m["gender"] == "女"]
    all_members = [m["name"] for m in members]

    # 指定只给男生抽的任务
    male_tasks = ["拖地", "窗户"]
    other_tasks = [t for t in tasks if t not in male_tasks]

    # 校验人数和任务数
    if len(male_members) < len(male_tasks):
        logger.error("男生人数不足，无法分配男生专属任务")
        return
    if len(all_members) != len(male_tasks) + len(other_tasks):
        logger.error("成员数量与任务数量不一致，无法分配卫生任务")
        return

    # 男生任务分配
    random.shuffle(male_members)
    random.shuffle(male_tasks)
    male_assign = dict(zip(male_members, male_tasks))

    # 剩余成员和任务
    assigned_males = set(male_assign.keys())
    left_members = [m for m in all_members if m not in assigned_males]
    random.shuffle(other_tasks)
    other_assign = dict(zip(left_members, other_tasks))

    # 汇总结果
    result_lines = []
    week_map = ["一", "二", "三", "四", "五", "六", "日"]
    now = time.localtime()
    date_str = time.strftime("%Y-%m-%d", now)
    week_str = week_map[now.tm_wday]
    result_lines.append(f"【{date_str} 星期{week_str}】")

    for name in all_members:
        if name in male_assign:
            result_lines.append(f"{name}------{male_assign[name]}")
        else:
            result_lines.append(f"{name}------{other_assign[name]}")

    # 组装飞书消息
    timestamp = str(round(time.time()))
    secret = Config["feishu"]["secret"]
    sign_val = sign(timestamp, secret).gen_sign()
    content_blocks = []
    for line in result_lines:
        content_blocks.append([{"tag": "text", "text": line}])
    # @所有人
    content_blocks.append([
        {
            "tag": "at",
            "user_id": "all",
            "user_name": "所有人"
        }
    ])
    message_body = {
        "timestamp": timestamp,
        "sign": sign_val,
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "今天自清洁抽签结果，恭喜同学们：",
                    "content": content_blocks
                }
            }
        }
    }
    response_message = feishu_robot(Config["feishu"]["webhook"], message_body).push()
    logger.info("卫生抽签推送结果：" + str(response_message))



# # 启动定时任务
# if __name__ == "__main__":
#     # BlockingScheduler
#     scheduler = BlockingScheduler(timezone="Asia/Shanghai")
#     # 添加定时任务：每周五11点
#     scheduler.add_job(
#         cleaning_lottery_job,
#         'cron',
#         day_of_week=Config["cleaning_lottery"]["week"],
#         hour=Config["cleaning_lottery"]["hour"],
#         minute=Config["cleaning_lottery"]["minute"]
#     )
#     scheduler.start()

# 直接运行一次用于测试
cleaning_lottery_job()