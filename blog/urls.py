# -*- coding = utf-8 -*-
# @Time : 2024/10/29 15:47
# @Author : Cat_E
# @File : urls.py
# @Software : PyCharm


from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('jingang', views.index, name='index'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog/pub', views.pub_blog, name='pub_blog'),
]


