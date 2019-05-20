from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from . import models,utils


# Create your views here.
@utils.login_user
def index(request):
    if request.method == 'GET':
        question = models.Poll.objects.all()
        print(question)
        return render(request, 'poll/index.html', {'msg': "请选择你要投票的内容", 'question': question})

@utils.login_user
def add(request):
    if request.method == 'GET':
        return render(request, 'poll/add.html', {'msg': "请在下方填写内容"})
    else:
        question = request.POST['questions'].strip()
        option_one = request.POST['option_one'].strip()
        option_two = request.POST['option_two'].strip()
        if len(question) == 0:
            return render(request, 'poll/add.html', {'msg': "投票内容不能为空！"})
        if len(option_one) == 0:
            return render(request, 'poll/add.html', {'msg': "选项一不能为空！"})
        if len(option_two) == 0:
            return render(request, 'poll/add.html', {'msg': "选项二不能为空！"})

        try:
            models.Poll.objects.get(questions=question)
            return render(request, 'poll/add.html', {'msg': "已经存在该问题不能重复添加！"})
        except:
            poll = models.Poll(questions=question, option_one=option_one, option_two=option_two)
            try:
                poll.save()
                # return render(request,'poll/index.html', {'msg': "发起投票成功！"})
                return redirect(reverse('poll:index'))
            except Exception as e:
                print('捕获错误信息：', e)
                return render(request, 'poll/add.html', {'msg': "发起投票失败！"})

@utils.login_user
def vote(request, q_id):
    poll = models.Poll.objects.get(pk=q_id)
    if request.method == 'GET':
        return render(request, 'poll/vote.html', {'poll': poll})
    else:
        option = request.POST['option']
        if option == '1':
            poll.poll_one += 1
            poll.save()
        else:
            poll.poll_two += 1
            poll.save()
        return redirect(reverse('poll:detail', kwargs={'q_id': poll.id}))

@utils.login_user
def detail(request, q_id):
    poll = models.Poll.objects.get(pk=q_id)
    if request.method == 'GET':
        return render(request, 'poll/detail.html', {'poll': poll})

def reg(request):
    if request.method=='GET':
        return render(request,'poll/reg.html',{'msg':'请注册！'})
    else:
        name=request.POST['name'].strip()
        pwd=request.POST['pwd'].strip()

        if len(name)==0:
            return render(request, 'poll/reg.html', {'msg': '用户名不能为空！'})
        if len(pwd)==0:
            return render(request, 'poll/reg.html', {'msg': '密码不能为空！'})
        try:
            user=models.User.objects.get(name=name)
            return render(request, 'poll/reg.html', {'msg': '该用户名已经存在！'})
        except Exception as e:
            print('捕获错误信息：',e)
            user=models.User(name=name,pwd=pwd)
            user.save()
            return render(request, 'poll/login.html', {'msg': '注册成功，请登录！'})

def login(request):
    if request.method=='GET':
        return render(request,'poll/login.html',{'msg':'请登录！'})
    else:
        name=request.POST['name'].strip()
        pwd=request.POST['pwd'].strip()

        try:
            user=models.User.objects.get(name=name,pwd=pwd)
            # 把用户信息加入到session
            request.session['login_user'] = user
            return redirect(reverse('poll:index'))
        except Exception as e:
            print('捕获错误信息：',e)
            return render(request, 'poll/login.html', {'msg': '用户名或密码错误！'})
@utils.login_user
def logout(request):
    del request.session['login_user']
    return render(request,'poll/login.html',{'msg':'账号已经退出请重新登录！'})