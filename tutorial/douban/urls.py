# -*- coding:utf-8 -*-
# 作者：庄立成
# 日期：2020/6/10 18:15
# 工具：PyCharm
# 文件 :urls.py
# Python版本：3.5.2
from django.conf.urls import url
from douban import views
urlpatterns = [
    url(r'^actors/$', views.ActorsList),
    url(r'^actors/(?P<pk>[0-9]+)/$', views.ActorDetail),
]