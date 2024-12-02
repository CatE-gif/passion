# -*- coding = utf-8 -*-
# @Time : 2024/11/12 17:04
# @Author : Cat_E
# @File : forms.py
# @Software : PyCharm
from os.path import exists

from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

user = get_user_model()

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=3, error_messages={'required':"请输入用户名",
                                                                            "min_length":3,
                                                                            "max_length":50})
    email = forms.EmailField(error_messages={'required':"请输入邮箱",
                                             'invalid':"请传入一个正确邮箱"})
    captcha = forms.CharField(max_length=4, min_length=4)
    password = forms.CharField(max_length=20, min_length=2)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = user.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("此邮箱已经注册")
        else:
            return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')

        captcha_modle = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_modle:
            raise forms.ValidationError("验证码错误")
        else:
            captcha_modle.delete()
            return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required':"请输入邮箱",
                                             'invalid':"请传入一个正确邮箱"})
    password = forms.CharField(max_length=20, min_length=2)
    remember = forms.IntegerField(required=False)





