from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        template = loader.get_template('signup.html')
        return HttpResponse(template.render())
