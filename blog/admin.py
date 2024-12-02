from django.contrib import admin
from .models import Blog, BlogCategory, BlogComments

# Register your models here.


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date', 'category', 'author']

class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ['content', 'pub_date', 'author', 'blog']

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogComments, BlogCommentsAdmin)


