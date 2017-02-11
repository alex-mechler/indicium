from .models import User
from django.shortcuts import render
from django.http import HttpResponse
import request_id

# Create your views here.
def settings(request):
    uid = request_id.get_id(request)
    if uid:
        user_row = User.objects.filter(id=uid)
        return HttpResponse(user_row.email)
    return HttpResponse("The user is not authenticated")
