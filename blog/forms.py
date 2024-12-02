# # -*- coding = utf-8 -*-
# # @Time : 2024/11/25 16:10
# # @Author : Cat_E
# # @File : forms.py
# # @Software : PyCharm
# # from django import forms
# #
# #
# # class PubBlogForm(forms.Form):
# #     title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
# #     content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
# #     category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
# #
#
#
#
# from django import forms
# from .models import BlogCategory  # 确保导入了对应的模型
#
# class PubBlogForm(forms.Form):
#     title = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=100,
#         required=True,
#         label="标题"
#     )
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         required=True,
#         label="内容"
#     )
#     category = forms.ModelChoiceField(
#         queryset=BlogCategory.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         required=True,
#         label="分类"
#     )
#
#


from django import forms
from .models import BlogCategory

class PubBlogForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)  # 使用 Textarea 小部件处理富文本内容
    category = forms.ModelChoiceField(queryset=BlogCategory.objects.all())

    # title = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入标题'}),
    #     max_length=100,
    #     required=True,
    #     label="标题"
    # )
    # content = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '请输入内容'}),
    #     required=True,
    #     label="内容"
    # )
    # category = forms.ModelChoiceField(
    #     queryset=BlogCategory.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-select'}),
    #     required=True,
    #     label="分类"
    # )


from django import forms
from .models import Blog


