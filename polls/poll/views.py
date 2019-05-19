from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from . import models


# Create your views here.
def index(request):
    if request.method == 'GET':
        question = models.Poll.objects.all()
        print(question)
        return render(request, 'poll/index.html', {'msg': "请选择你要投票的内容", 'question': question})


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


def detail(request, q_id):
    poll = models.Poll.objects.get(pk=q_id)
    if request.method == 'GET':
        return render(request, 'poll/detail.html', {'poll': poll})
