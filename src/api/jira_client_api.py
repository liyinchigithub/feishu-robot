#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from jira import JIRA
from util.get_json import config
# 读取配置文件
Config = config("../../config/config.json").get_config_from_json()
UserInfo = config("../../config/userInfo.json").get_config_from_json()
# jira初始化
url = Config["jira"]["url"]
auth = (Config["jira"]["username"], Config["jira"]["password"])  # jira登录账号和密码
jira = JIRA(auth=auth, options={'server': url})


"""
    @Time :2022/02/11
    @Author :liyinchi
    @File :jira_get.py
    @Version：1.0
"""


class jira_get():
    def __init__(self):
        pass
    """
        [jira所有项目名称]
        :param none
        :return: list
    """
    def get_projects(seft):
        projects = jira.projects()
        print(projects)
        return projects
    """
        [获取issue信息]
        :param 'JRA-1330'
        :return: list
    """
    def get_issue(issue_id):
        issue = jira.issue(issue_id)
        return issue
    """
        [issue添加关注者]
        :param issue 例如：'JRA-1330'
        :param username 例如：'liyc'
        :return: list
    """
    def add_watcher_issue(issue, username):
        jira.add_watcher(issue, username)

    """
        [获取issue所有关注者]
        :param issue 例如：'JRA-1330'
        :return: list
    """
    def get_watcher_issue(issue):
        print(jira.watchers(issue))
        return jira.watchers(issue)
    """
        [获取issue所有评论]
        :param issue 例如：'JRA-1330'
        :return: list
    """
    def get_comment_all_issue(issue):
        print(jira.comments(issue))
        return jira.comments(issue)
    """
        [issue获取某条评论]
        :param issue 例如：'JRA-1330'
        :param comment_id 例如：'10234'
        :return: list
    """
    def get_comment_issue(issue, comment_id):
        return jira.comment(issue, comment_id)
    """
        [issue新增评论]
        :param issue 例如：'JRA-1330'
        :param comment_id 例如：'10234'
        :return: list
    """
    def add_comment_issue(issue, text):
        jira.add_comment(issue, 'new comment')
    """
        [issu更新评论]
        :param issue 例如：'JRA-1330'
        :param comment_id 例如：'10234'
        :return: list
    """
    def update_comment_issue(issue, comment_id, text):
        comment = jira.comment(issue, comment_id)
        return comment.update(body=text)  # 更新评论
    """
        [issue删除评论]
        :param issue 例如：'JRA-1330'
        :param comment_id 例如：'10234'
        :return: list
    """
    def delete_comment_issue(issue, comment_id):  # comment_id:'10234'
        comment = jira.comment(issue, comment_id)  # 某条评论
        comment.delete()  # 删除该评论
    """
        [获取issue附件]
        :param issue 例如：'JRA-1330'
        :return: list
    """    
    def get_attachment_issue(issue):
        print(issue.fields.attachment)  # 问题附件
        return issue.fields.attachment
    
    """
        [issue添加附件]
        :param issue 例如：'JRA-1330'
        :param attachment 例如：'/some/path/attachment.txt'
        :return: list
    """  
    def add_attachment_issue(issue, attachment):
        jira.add_attachment(
            issue, attachment=attachment)  # 添加附件

    """
        创建issue
        :param issue_dict 例如：issue_dict = {
                                            'project': {'id': 123},
                                            'summary': 'New issue from jira-python',
                                            'description': 'Look into this one',
                                            'issuetype': {'name': 'Bug'},
                                        }
        :return: none
    """  
    def add_issue(issue_dict):
        jira.create_issue(fields=issue_dict)
    """
        [批量创建issue]
        :param issue_dict 例如：issue_list = [
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
        :return: none
    """         
    def add_issues(issue_list):
        jira.create_issues(field_list=issue_list)    
    # 分配问题
    def add_issues(issue,newassignee):
        jira.assign_issue(issue, newassignee)


    # 转换问题
    # jira.transition_issue(issue, '5', assignee={'name': 'pm_user'}, resolution={'id': '3'})
    """
        [搜索issue]
        Jira的搜索非常强大，并配有一套专门的搜索语言，称为JQL(Jira Query Language)，Jira的Python库便是基于JQL语法进行搜索的，返回的是搜索到的问题列表。
        默认最大结果数未1000，可以通过maxResults参数配置，该参数为-1时不限制数量，返回所有搜索结果。
        :param jql jirajql语句
        :return list
    """
    def search_issue(jql):
        return jira.search_issues(jql, maxResults=-1)

'''
        [创建/分配/转换问题]
        jira.create_issue(): 创建问题
        jira.create_issues(): 批量创建问题
        jira.assign_issue(): 分配问题
        jira.transitions(): 获取问题的工作流
        jira.transition_issue(): 转换问题
        [关注者/评论/附件]
        jira.watchers(): 问题的关注者
        jira.add_watcher(): 添加关注者
        jira.remove_watcher(): 移除关注者
        jira.comments(): 问题的所有评论
        jira.comment(): 某条评论
        jira.add_comment()：添加评论
        comment.update()/delete(): 更新/删除评论
        jira.add_attachment(): 添加附件

'''