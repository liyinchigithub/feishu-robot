#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from jira import JIRA

url = 'http://jira.***.com/'

auth = ("username", "password")#  jira登录账号和密码

jira = JIRA(auth=auth, options={'server': url})
issue = jira.issue('JRA-1330')
'''
关注者/评论/附件#
jira.watchers(): 问题的关注者
jira.add_watcher(): 添加关注者
jira.remove_watcher(): 移除关注者
jira.comments(): 问题的所有评论
jira.comment(): 某条评论
jira.add_comment()：添加评论
comment.update()/delete(): 更新/删除评论
jira.add_attachment(): 添加附件
'''

print(jira.watchers(issue)) # 所有关注者
jira.add_watcher(issue, 'username')  # 添加关注者

print(jira.comments(issue))  # 所有评论
comment = jira.comment(issue, '10234')  # 某条评论
jira.add_comment(issue, 'new comment') # 新增评论
comment.update(body='update comment')  # 更新评论
comment.delete()  # 删除该评论

print(issue.fields.attachment)  # 问题附件
jira.add_attachment(issue=issue, attachment='/some/path/attachment.txt')  # 添加附件
