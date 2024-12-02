# -*- coding = utf-8 -*-
# @Time : 2024/11/4 23:31
# @Author : Cat_E
# @File : urls.py
# @Software : PyCharm
from tkinter import image_names

from django.urls import path
from . import views

app_name = 'xlauth'

urlpatterns = [
    path('login', views.xllogin, name='login'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='captcha'),
    path('test2', views.test2, name='text2'),
    path('logout', views.xllogout, name='logout'),
]



