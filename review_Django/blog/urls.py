# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 7:33 上午
# @Author  : AI悦创
# @FileName: urls.py.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index')
	# path(route, view)
	# path(route, view, name="'index'")
]

# 单词 route
"""
n. 路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；（北美）递送路线；用于美国干线公路号码前
v. 按特定路线发送，为……规定路线
"""
