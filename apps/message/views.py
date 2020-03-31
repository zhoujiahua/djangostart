#!/usr/bin/python3

from django.shortcuts import render
from datetime import datetime

from .models import UserMessage


# Home page
def home_page(request):
    return render(request, 'views/index.html')


# Create your views here.
def get_form(request):
    # 查询数据
    # all_message = UserMessage.objects.all()
    # all_message = UserMessage.objects.filter(name='jiahua', address='北京')  # 条件查询
    # print(all_message)
    # for msg in all_message:
    #     print(msg.email)

    # 数据保存
    # user_message = UserMessage()
    # user_message.name = 'Jerry'
    # user_message.email = 'jerry@163.com'
    # user_message.address = '上海'
    # user_message.message = 'Welcome to Shanghai'
    # user_message.object_id = 'shanghai123'
    # user_message.save()

    # 获取POST数据
    # if request.method == 'POST':
    #     user_message = UserMessage()
    #     user_message.name = request.POST.get('name', '')
    #     user_message.email = request.POST.get('email', '')
    #     user_message.address = request.POST.get('address', '')
    #     user_message.message = request.POST.get('message', '')
    #     user_message.object_id = datetime.now()
    #     user_message.save()

    # 删除数据
    # all_message = UserMessage.objects.all()
    # all_message.delete() #删除全部数据
    all_message = UserMessage.objects.filter(name='weqr')  # 条件删除
    for msg in all_message:
        msg.delete()
    return render(request, 'msg_form.html', {'message': 'Welcome to django'})
