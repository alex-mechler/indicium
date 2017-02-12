from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        template = loader.get_template('login.html')
        return HttpResponse(template.render())
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/dashboard")
#             return HttpResponse('Thanks for loging in ' + username)
        else:
            return HttpResponse('failed')
