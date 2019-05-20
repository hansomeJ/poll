from django.shortcuts import redirect
from django.shortcuts import reverse

def index(request):
    if request.method=='GET':
        return redirect(reverse("poll:reg"))