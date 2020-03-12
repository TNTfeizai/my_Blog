# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import User


# 登录视图

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = User.objects.filter(username=user_name)  # 查看数据库里是否有该用户名
        if user:  # 如果存在
            user = User.objects.get(username=user_name)  # 读取该用户信息
            if pass_word == user.password:  # 检查密码是否匹配
                request.session['IS_LOGIN'] = True
                request.session['nickname'] = user.nickname
                request.session['username'] = user_name
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'login.html', {'error': '密码错误!'})
        else:
            return render(request, 'login.html', {'error': '用户名不存在!'})


# 注册
class RegisterView(View):
    def get(self,request):
        return render(request, 'register.html')

    def post(self, request):
        user_name = request.POST.get('username', '')
        pass_word_1 = request.POST.get('password_1', '')
        pass_word_2 = request.POST.get('password_2', '')
        nick_name = request.POST.get('nickname', '')
        email = request.POST.get('email', '')
        avatar = request.FILES.get('avatar')
        if User.objects.filter(username=user_name):
            return render(request, 'register.html', {'error': '用户已存在'})
            # 将表单写入数据库
        if (pass_word_1 != pass_word_2):
            return render(request, 'register.html', {'error': '两次密码请输入一致'})
        user = User()
        user.password = pass_word_1
        user.email = email
        user.nickname = nick_name
        user.save()
        # 返回注册成功页面
        return render(request, 'login.html')


# 详情页
class LoginsuccessView(View):
    def post(self, request):
        username = request.POST.get('username', '')
        return render(request, 'detail.html',context={'username':username})
