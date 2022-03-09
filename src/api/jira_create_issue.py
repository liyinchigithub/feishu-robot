#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from jira import JIRA

url = 'http://jira.***.com/'

auth = ("username", "password")#  jira登录账号和密码

jira = JIRA(auth=auth, options={'server': url})

'''
创建/分配/转换问题#
jira.create_issue(): 创建问题
jira.create_issues(): 批量创建问题
jira.assign_issue(): 分配问题
jira.transitions(): 获取问题的工作流
jira.transition_issue(): 转换问题
'''

# 创建问题
issue_dict = {
    'project': {'id': 123},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
}
new_issue = jira.create_issue(fields=issue_dict)

# 批量创建问题
issue_list = [
{
    'project': {'id': 123},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
},
{
    'project': {'key': 'FOO'},
    'summary': 'Second issue',
    'description': 'Another one',
    'issuetype': {'name': 'Bug'},
},
{
    'project': {'name': 'Bar'},
    'summary': 'Last issue',
    'description': 'Final issue of batch.',
    'issuetype': {'name': 'Bug'},
}]
issues = jira.create_issues(field_list=issue_list)

# 分配问题
# jira.assign_issue(issue, 'newassignee')

# 转换问题
# jira.transition_issue(issue, '5', assignee={'name': 'pm_user'}, resolution={'id': '3'})

# 搜索issue
# Jira的搜索非常强大，并配有一套专门的搜索语言，称为JQL(Jira Query Language)，Jira的Python库便是基于JQL语法进行搜索的，返回的是搜索到的问题列表。
# 默认最大结果数未1000，可以通过maxResults参数配置，该参数为-1时不限制数量，返回所有搜索结果。
jira.search_issues('project=PROJ and assignee = currentUser()', maxResults=-1)