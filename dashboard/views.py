from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
import request_id

def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def settings(request):
    uid = request_id.get_id(request)
    template = loader.get_template('dashboard/settings.html')
    context = {}
    if uid:
        context['user_row'] = User.objects.get(pk=uid)
    return HttpResponse(template.render(context, request))

def post_settings(request):
    first_name = request.POST.get("first_name", None)
    last_name = request.POST.get("last_name", None)
    dob = request.POST.get("dob", None)
    email = request.POST.get("email", None)
    doctor_email = request.POST.get("doctor_email", None)
    # Get template
    template = loader.get_template('dashboard/success.html')
    context = {}
    # Update the database entry
    uid = request_id.get_id(request)
    if uid:
        user_row = User.objects.get(pk=uid)
        user_row.first_name = first_name
        user_row.last_name = last_name
        user_row.dob = dob
        user_row.email = email
        user_row.doctor_email = doctor_email
        user_row.save()
        context['successful'] = True
    return HttpResponse(template.render(context, request))

def post_password(request):
    # Get form input
    old_pass = request.POST.get("old_password", None)
    new_pass = request.POST.get("new_password", None)
    # Get template
    template = loader.get_template('dashboard/success.html')
    context = {}
    # Check the user's authentication
    u = request.user
    if u.is_authenticated() and u == authenticate(username=request.user.username, password=old_pass):
        # Change password
        u.set_password(new_pass)
        u.save()
        context['successful'] = True
    return HttpResponse(template.render(context, request))
