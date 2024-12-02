from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '博客分类'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '博客'

class BlogComments(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '博客评论'