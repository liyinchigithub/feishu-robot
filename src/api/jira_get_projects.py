#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from jira import JIRA

url = 'http://jira.***.com/'

auth = ("username", "password")#  jira登录账号和密码

jira = JIRA(auth=auth, options={'server': url})
projects = jira.projects()
print(projects)

