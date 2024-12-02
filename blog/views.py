from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.views.decorators.http import require_http_methods
from .models import Blog, BlogCategory, BlogComments
from .forms import PubBlogForm
from django.http.response import JsonResponse


# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by("-pub_date")
    return render(request, 'index.html', context={'blogs': blogs})


def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        blog = None
    return render(request, 'blog_detail.html', {'blog': blog})

@require_http_methods(['GET', 'POST'])
@login_required(login_url='/auth/login')
def pub_blog(request):
    form = PubBlogForm(request.POST)
    print("Request POST data:", request.POST)  # 打印提交的数据
    print("Form valid:", form.is_valid())  # 打印验证结果
    print("Form errors:", form.errors)  # 打印表单错误信息

    if request.method == 'GET':
        category = BlogCategory.objects.all()
        return render(request, 'pub_blog.html', {"category": category})
    else:
        form = PubBlogForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            blog = Blog.objects.create(title=title, content=content, category=category, author=request.user)
            return JsonResponse({'code': 200, 'message': "发布成功！", "data": {"blog_id": blog.id}})
        else:
            # print(form.errors)
            return JsonResponse({'code': 400, 'message': form.errors})



