from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
