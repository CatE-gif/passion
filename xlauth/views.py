from lib2to3.pygram import python_grammar_no_print_statement
from xml.dom import HierarchyRequestErr

from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
import string, random
from django.core.mail import send_mail
from django.utils.log import request_logger
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()

# Create your views here.

@require_http_methods(['GET', 'POST'])
def xllogin(request):
    print("11111.", request.method)
    if request.method == 'GET':
        print("GET")
        return render(request, 'login.html')
    else:
        print("POST")
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            print(email, password)
            if user and user.check_password(password):
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect('/')
            else:
                print("邮箱或者密码错误")
                return JsonResponse({"error": "邮箱或者密码错误"}, status=400)  # 返回错误信息


def xllogout(request):
    logout(request)
    return redirect('/')


@require_http_methods(['GET', 'POST'])
def register(request):
    print("11111." , request.method)


    if request.method == 'GET':
        print("get请求")
        return render(request, 'register.html')
    else:
        form = RegistrationForm(request.POST)
        print("post")
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            print("进来:",email,username,password)
            return redirect(reverse('xlauth:login'))
        else:
            print(form.errors)
            return redirect(reverse('xlauth:register'))


def send_email_captcha(request):
    email = request.GET.get('email')
    # print(email)
    if not email:
        return JsonResponse({'code':400, 'message':'必须传递邮箱！'})
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("注册验证码", message=f"您的验证码为{captcha}, 打死也不要告诉别人！！", from_email="3147272673@qq.com", recipient_list=[email], fail_silently=False)
    # send_mail("注册验证码", message=f"您的验证码为{captcha}, 打死也不要告诉别人！！", fail_silently = False)

    return JsonResponse({'code':200, 'message':"验证码发送成功！"})

def test2(request):
    return render(request, 'test2.html')