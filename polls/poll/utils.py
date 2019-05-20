from django.shortcuts import render

def login_user(fn):
    def inner(request,*args,**kwargs):
        login_user=request.session.get('login_user',None)
        if login_user is not None:
            return fn(request,*args,**kwargs)
        else:
            return render(request,'poll/login.html',{'msg':'该页面登录后才能访问！'})
    return inner