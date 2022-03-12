#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from jira import JIRA

url = 'https://jira.xxx.com'

auth = ("", "")#  jira登录账号和密码

jira = JIRA(auth=auth, options={'server': url})

# 查询问题，支持JQL语句
# 当前用户创建的bug且状态为“已关闭”状态
# closed_issues = jira.search_issues('status = 已关闭 AND creator in (currentUser()) ORDER BY priority DESC, updated DESC', maxResults=-1)
# 当前用户创建的bug且状态为“激活”状态
# open_issues = jira.search_issues('status = 激活 AND creator in (currentUser()) ORDER BY priority DESC, updated DESC')# 激活、已关闭、已解决
# 最近一周
last_week_issues = jira.search_issues('creator in (currentUser()) AND created >= -1w ORDER BY priority DESC, updated DESC')# 激活、已关闭、已解决

# 注意：如果不加maxResults=-1参数，则实际总数大于50时只能查出50条数据。
# print("closed_issues:",closed_issues)
# print("open_issues:",open_issues)# 返回数组
# print("open_issues:",open_issues[0].id)#  type(open_issues)为 <class 'jira.client.ResultList'>
# print("closed_issues:",len(closed_issues))
# print("open_issues:",len(open_issues))
print("last_week_issues:",len(last_week_issues))
print("last_week_issues:",last_week_issues)