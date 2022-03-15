# feishu-robot

[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-374/) [![pip](https://img.shields.io/badge/pip-22.0.4-yellow.svg)](https://pip.pypa.io/en/stable/)[![jira](https://img.shields.io/badge/JIRA-v8.12.0-blue.svg)](https://www.atlassian.com/software/jira)

 

飞书机器人，每日发送测试人员缺陷情况到飞书群

<img width="400"  height="400" alt="image" src="https://user-images.githubusercontent.com/19643260/158024815-9871c401-d023-41cf-bc4e-b99445469946.png">


# 环境要求
|环境|版本|
|-|-|
|python|3.7.4|
|pip|22.0.4|
 
 
## 更新pip

```python
pip install --upgrade pip
```

## 创建虚拟目录

```shell
# python -m venv 虚拟环境名称，名称是随意起的
python -m venv tutorial-env
```

## 激活虚拟环境

* 当激活虚拟环境时命令行上会有个虚拟环境名前缀

#### Unix或MacOS上激活虚拟环境
```shell
source tutorial-env/bin/activate
```
#### windows上激活虚拟环境
```shell
tutorial-env\Scripts\activate.bat
```

### 项目依赖安装
```shell
python3.7 -m pip install --upgrade pip
pip install -r requirements.txt
```

* 如果引入其他新的依赖，可以执行冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```
* 如果pip不起作用，可以从pypi上下载最新的源码包(https://pypi.python.org/pypi/)进行安装：
```shell
python setup.py install 
```


# 项目使用说明

## 1.修改配置

（1）配置jira、飞书机器人
>config/config.json
```json
{
    "jira": {
        "url": "https://jira.xxxx.com", jira地址
        "url_browse": "https://jira.xxxx.com/browse/",  用于机器人发送消息模板点击链接地址
        "username": "", jira账号
        "password": ""  jira密码
    },
    "feishu": {
        "webhook": "https://open.feishu.cn/open-apis/bot/v2/hook/xxxx", 飞书机器人webhook
        "secret":"xxxx"  飞书机器人秘钥
    },
    "timing_task":{
        "week":"1-5",    每周一至五
        "hour":9,        上午9点30分执行一次
        "minute":30         
    }
}
```
（2）jira账号和姓名（配置测试团队成员）
>config/userInfo.json

```json
{
    "userInfo":[
        { "username": "wangml", "name": "王美玲" },
        { "username": "chenyaojie", "name": "陈耀杰" },
        { "username": "liancm", "name": "练春木" },
        { "username": "linzx", "name": "林志祥" },
        { "username": "wangjunq", "name": "王俊奇" },
        { "username": "xuby", "name": "许冰艳" },
        { "username": "kanglt", "name": "康丽婷" },
        { "username": "liyc", "name": "李银池" }
    ]
    
}
```

# 运行脚本

## 单元测试

* pytest
```shell
pytest
```
* unittest
```shell
python -m unittest -v src.test.unit_test.TestFeishuRobot
# python -m unittest 文件名.类名.方法名
```
[unittest](https://docs.python.org/zh-cn/3/library/unittest.html)
[测试报告](http://tungwaiyip.info/software/HTMLTestRunner.html)

## 定时任务
```
python main.py
```

## 服务器部署启动
第一种方式：
```shell
nohup python main.py >> feishu-robot-python-main.log 2>&1 &
```

第二种方式：使用pm2进程守护启动
<img width="1106" alt="image" src="https://user-images.githubusercontent.com/19643260/157842375-b126e2b9-74ce-4fc9-b07e-24706c95351f.png">

# 飞书机器人

[如何在群组中使用机器人？](https://www.feishu.cn/hc/zh-CN/articles/360024984973)

[飞书开放文档](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)

[消息内容](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json)


<img width="1439" alt="image" src="https://user-images.githubusercontent.com/19643260/157471462-13bbc85d-8c14-4884-a729-52f4eb248b47.png">

使用飞书机器人发送消息，本质是使用Python的requests类库发送http请求，请求地址即为创建机器时保存的webhook链接，发送的内容实际为json串，请求header为{'Content-Type': 'application/json; charset=utf-8'}

## 文本text

文本消息@用法说明
 // @ 单个用户
<at user_id="ou_xxx">名字</at>
// @ 所有人
<at user_id="all">所有人</at>

```json
{
    "receive_id": "oc_xxx",
    "content": " {\"text\":\"<at user_id=\\\"ou_xxx\\\">Tom</at> text content\"}",
    "msg_type": "text"
} 
```

>@单个用户时，user_id填open_id，必须是有效值，否则取名字展示，没有@效果；@所有人必须满足所在群开启@所有人功能。


## 飞书机器人-可发送的消息类型
自定义机器人添加完成后，就能向其 webhook 地址发送 POST 请求，从而在群聊中推送消息了。支持推送的消息格式有文本、富文本、图片消息，也可以分享群名片等。
参数msg_type代表消息类型，可传入：
text（文本）/ post（富文本）/ image（图片）/ share_chat（分享群名片）/ interactive（消息卡片）。具体使用方法可查看下文的官方文档。

## 飞书机器人-请求发送后的返回信息汇总
* 消息发送成功：{“Extra”:null,“StatusCode”:0,“StatusMessage”:“success”}
* webhook地址无效：{“code”:19001,“msg”:“param invalid: incoming webhook access token invalid”}
* 关键词校验失败：{“code”:19024,“msg”:“Key Words Not Found”}
* IP校验失败：{“code”:19022,“msg”:“Ip Not Allowed”}
* 签名校验失败：{“code”:19021,“msg”:“sign match fail or timestamp is not within one hour from current time”}

## 飞书机器人-常见问题
* 自定义机器人的 webhook地址有 V1、V2 版本，如何兼容？
答：请参考帮助文档如何在群聊中使用机器人的附录部分“旧版 webhook (自定义机器人) 使用说明”。同时，推荐使用V2版本的自定义机器人。
* 使用 webhook 的自定义机器人是否可以@单个成员、或者@所有人？
答：V2版本的自定义机器人，支持@单个成员、或者@所有人。
* 配置使用 webhook 的自定义机器人时，参数text是否有长度要求？
答：建议 JSON 的长度不超过 30k，序列化后的 pb 不超过 100k，图片最好小于 10MB。

## 机器人扩展应用场景
* 服务器监测报警
* 天气情况、生日提醒和新闻资讯等的推送
* 个人开发应用的用户反馈
* 轻量级的埋点统计



# 脚本解析

## jira数据获取

### 登录鉴权

Jira的访问是有权限的，在访问Jira项目时首先要进行认证，Jira Python库提供了3种认证方式：

* 通过Cookis方式认证（用户名，密码）
* 通过Basic Auth方式认证（用户名，密码）
* 通过OAuth方式认证
* 认证方式只需要选择一种即可，以下代码为使用Cookies方式认证。

请求
```python
    from jira import JIRA
    jira = JIRA(auth=("username", "pwd"), options={'server': 'https://**.**.**.**'})
    # 参数xauth不是通信协议的basic_auth，连接方式请参考文首最新的官方文档，其他文章均为basic_auth，导致连不上
    projects = jira.projects()
    print(projects)
```
输出：是一个数组，每个项目由<>包围，key是关键字，name是项目名

[<JIRA Project: key='NEW', name='***项目', id='10433'>, <JIRA Project: key='**', name='**', id='10467'>, <JIRA Project: key='***', name='***重构', id='10501'>, <JIRA Project: key='P2020021451', name='**', id='10502'>, <JIRA Project: key='***', name='**工作', id='10481'>, <JIRA Project: key='***', name='**工作', id='10490'>, <JIRA Project: key='**', name='**申请', id='10446'>, <JIRA Project: key='**', name='**', id='10613'>]
    
* 获取数组中每个元素下标的key
```
print("open_issues:",open_issues[0].key)#  type(open_issues)为 <class 'jira.client.ResultList'>
```
* 获取数组中每个元素下标的id
```
print("open_issues:",open_issues[0].id)#  type(open_issues)为 <class 'jira.client.ResultList'>
```

### 使用jira jql获取缺陷数据


* 查询每个bug的详细信息，需要加上fields参数
```python
# 查询问题，支持JQL语句,一定要增加json_result参数，会返回bug详细信息,fields为指定显示的字段
issues = jira.search_issues('project = P2020021451 AND component = 销售管理模块',  fields="summary, priority, status", maxResults=-1, json_result='true')

print(issues)
```
[可使用的字段]
* 项目project; 
* 模块名称components; 
* 标题summary; 
* 缺陷类型issuetype; 
* 具体描述内容description; 
* 经办人assignee; 
* 报告人reporter; 
* 解决结果resolution;
* bug状态status;
* 优先级priority;
* 创建时间created;
* 更新时间updated;
* 评论comments*

返回
```json
{
    'expand': 'schema,names',
    'startAt': 0,
    'maxResults': 1000,
    'total': 77,
    'issues': [{
        'expand': 'operations,versionedRepresentations,editmeta,changelog,renderedFields',
        'id': '66559',
        'self': 'https://jira.**.net.cn/rest/api/2/issue/66559',
        'key': 'P2020021451-173',
        'fields': {
            'summary': '***为非必填项',
            'priority': {
                'self': 'https://jira.**.net.cn/rest/api/2/priority/3',
                'iconUrl': 'https://jira.**.net.cn/images/icons/priorities/medium.svg',
                'name': '中',
                'id': '3'
            },
            'status': {
                'self': 'https://jira.**.net.cn/rest/api/2/status/10540',
                'description': '',
                'iconUrl': 'https://jira.**.net.cn/images/icons/statuses/generic.png',
                'name': '开发处理中',
                'id': '10540',
                'statusCategory': {
                    'self': 'https://jira.**.net.cn/rest/api/2/statuscategory/4',
                    'id': 4,
                    'key': 'indeterminate',
                    'colorName': 'yellow',
                    'name': '处理中'
                }
            }
        }
    }, {
        'expand': 'operations,versionedRepresentations,editmeta,changelog,renderedFields',
        'id': '57443',
        'self': 'https://jira.**.net.cn/rest/api/2/issue/57443',
        'key': 'P2020021451-4',
        'fields': {
            'summary': '**开发功能',
            'priority': {
                'self': 'https://jira.**.net.cn/rest/api/2/priority/2',
                'iconUrl': 'https://jira.**.net.cn/images/icons/priorities/high.svg',
                'name': '高',
                'id': '2'
            },
            'status': {
                'self': 'https://jira.**.net.cn/rest/api/2/status/10332',
                'description': '',
                'iconUrl': 'https://jira.**.net.cn/images/icons/statuses/generic.png',
                'name': '需求完成',
                'id': '10332',
                'statusCategory': {
                    'self': 'https://jira.**.net.cn/rest/api/2/statuscategory/3',
                    'id': 3,
                    'key': 'done',
                    'colorName': 'green',
                    'name': '完成'
                }
            }
        }
    }]
}
```

### 返回的jira对象便可以对Jira进行操作，主要的操作包括:
* 1.项目
* 2.问题
* 3.搜索
* 4.关注者
* 5.评论
* 6.附件
* 7.项目（Project）#
* 8.jira.projects(): 查看所有项目列表
* 9.jira.project("项目的Key"): 查看单个项目

#### 项目对象的主要属性及方法
    key: 项目的Key
    name: 项目名称
    description: 项目描述
    lead: 项目负责人
    projectCategory: 项目分类
    components: 项目组件
    versions: 项目中的版本
    raw: 项目的原始API数据

##### 1.项目
```python
print(jira.projects())  # 打印所有你有权限访问的项目列表

project = jira.project('某个项目的Key')

print(project.key, project.name, project.lead) 
```

##### 2.问题（Issue）

Issue是Jira的核心，Jira中的任务，用户Story，Bug实质上都是一个Issue。

单个问题对象可以通过jira.issue("问题的Key")得到，问题的主要属性和方法如下：

    id: 问题的id
    key: 问题的Key
    permalink(): 获取问题连接
    fields: 问题的描述，创建时间等所有的配置域
    raw: 问题的原始API数据

##### 3.配置域（Fields）

一般问题的ields中的属性分为固定属性和自定义属性，自定义属性格式一般为类似customfield_10012这种。常用的问题的Fields有：

    assignee：经办人
    created: 创建时间
    creator: 创建人
    labels: 标签
    priorit: 优先级
    progress:
    project: 所示项目
    reporter: 报告人
    status: 状态
    summary: 问题描述
    worklog: 活动日志
    updated: 更新时间
    watches: 关注者
    comments: 评论
    resolution: 解决方案
    subtasks: 子任务
    issuelinks: 连接问题
    lastViewed: 最近查看时间
    attachment

```
issue = jira.issue('JRA-1330')
print(issue.key, issue.fields.summary, issue.fields.status)
```
##### 4.关注者/评论/附件

    jira.watchers(): 问题的关注者
    jira.add_watcher(): 添加关注者
    jira.remove_watcher(): 移除关注者
    jira.comments(): 问题的所有评论
    jira.comment(): 某条评论
    jira.add_comment()：添加评论
    comment.update()/delete(): 更新/删除评论
    jira.add_attachment(): 添加附件


```python
issue = jira.issue('JRA-1330')

print(jiaa.watchers(issue)) # 所有关注者
jira.add_watcher(issue, 'username')  # 添加关注者

print(jira.comments(issue))  # 所有评论
comment = jira.comment(issue, '10234')  # 某条评论
jira.add_comment(issue, 'new comment') # 新增评论
comment.update(body='update comment')  # 更新评论
comment.delete()  # 删除该评论

print(issue.fields.attachment)  # 问题附件
jira.add_attachment(issue=issue, attachment='/some/path/attachment.txt')  # 添加附件
```

##### 5.创建/分配/转换问题

jira.create_issue(): 创建问题
jira.create_issues(): 批量创建问题
jira.assign_issue(): 分配问题
jira.transitions(): 获取问题的工作流
jira.transition_issue(): 转换问题

```python
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
jira.assign_issue(issue, 'newassignee')

# 转换问题
jira.transition_issue(issue, '5', assignee={'name': 'pm_user'}, resolution={'id': '3'})
```

##### 6.搜索

Jira的搜索非常强大，并配有一套专门的搜索语言，称为JQL(Jira Query Language)，Jira的Python库便是基于JQL语法进行搜索的，返回的是搜索到的问题列表。

```python
jira.search_issues('JQL语句')
#默认最大结果数未1000，可以通过maxResults参数配置，该参数为-1时不限制数量，返回所有搜索结果。

jira.search_issues('project=PROJ and assignee = currentUser()', maxResults=-1)
```


通过python内置的dir()方法解析出每个事件都有哪些属性(字段),然后从中找出我们需要获取的数据,保存下来.

dir(i),dir(i.fields)运行结果示例(里面列出了事件的属性)
