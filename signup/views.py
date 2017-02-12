from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import request_id
from database.models import User as CustUser


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        template = loader.get_template('signup.html')
        return HttpResponse(template.render())
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm', '')
        dob = request.POST.get('dob', '')
        email = request.POST.get('email', '')
        firstname = request.POST.get('Fname', '')
        lastname = request.POST.get('Lname', '')
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()

        uid = request_id.get_id(request)
        u = CustUser(id=uid, control_id=uid, first_name=firstname, last_name=last_name, dob=dob, email=email)
        u.save()
