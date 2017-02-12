from .models import User, Symptoms
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.core.mail import send_mail
import request_id

def index(request):

    uid = request_id.get_id(request)
    if not uid:
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":'You need to <a href= "../login">Login</a>  before you can continue.'}, request))
    """Handles the editing of user symptoms"""

    # Perform action if requested
    if request.method == 'POST':
        if request.POST.get("send_action", None) != None:
            # Get user information
            u = User.objects.get(pk=uid)
            if(u.doctor_email is None or '@' not in u.doctor_email):
                template = loader.get_template('dashboard/message.html')
                return HttpResponse(template.render({"message":'You need to <a href= "../dashboard/settings">set a doctors email</a> before you can send them an email!'}, request))
            # Construct email from selected symptoms
            text = "Here is a table of " + u.first_name + " " + u.last_name + "'s symptoms:\n==============================\n"
            for item in request.POST:
                if item[:5]=="start":
                    row = Symptoms.objects.filter(user_id=uid, start=item[5:])[0]
                    items = {
                        "symptom" : row.symptom,
                        "location" : row.location,
                        "intensity": str(row.intensity),
                        "start": str(row.start),
                        "end": str(row.end),
                        "comments": row.comments,
                        "img_url": row.img_url,
                    }
                    text += "\n".join((i+": "+items[i]) for i in items if items[i]) + "\n\n===========================\n\n"
            # Send email
            send_mail(subject='Patient Symptoms',
                      message=text,
                      from_email='reports@indiciumapp.com',
                      recipient_list=[u.doctor_email])

    # Otherwise, just respond with dashboard
    template = loader.get_template('dashboard/index.html')
    # Load symptoms
    uid = request_id.get_id(request)
    context = {"symptoms" : Symptoms.objects.filter(user_id=uid)}
    return HttpResponse(template.render(context, request))

def dependants(request):
    # Check that the user is authenticated first
    uid = request_id.get_id(request)
    if not uid:
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":"You need to log in before you can continue."}, request))

    # Handle request
    template = loader.get_template('dashboard/dependants.html')
    return HttpResponse(template.render({}, request))

def settings(request):
    """Handles the editing of user settings"""

    # Check that the user is authenticated first
    uid = request_id.get_id(request)
    if not uid:
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":"You need to log in before you can continue."}, request))

    # Handle GET request
    if request.method == 'GET':
        template = loader.get_template('dashboard/settings.html')
        context = {"user_row": User.objects.get(pk=uid)}
        return HttpResponse(template.render(context, request))

    # Handle POST request
    first_name = request.POST.get("first_name", None)
    last_name = request.POST.get("last_name", None)
    dob = request.POST.get("dob", None)
    email = request.POST.get("email", None)
    doctor_email = request.POST.get("doctor_email", None)
    # Validate the input
    if "@" not in email:
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":"You must provide a valid email."}, request))
    # Update the database entry
    user_row = User.objects.get(pk=uid)
    user_row.first_name = first_name
    user_row.last_name = last_name
    user_row.dob = dob
    user_row.email = email
    user_row.doctor_email = doctor_email
    user_row.save()
    # Send response
    template = loader.get_template('dashboard/message.html')
    context = {"message":"Your information was updated successfully!"}
    return HttpResponse(template.render(context, request))

def new_symptom(request):
    # Check that the user is authenticated first
    uid = request_id.get_id(request)
    if not uid:
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":"You need to log in before you can continue."}, request))

    # Handle GET request
    if request.method == 'GET':
        template = loader.get_template('dashboard/newsymptom.html')
        return HttpResponse(template.render({}, request))

    # Handle POST request
    symptom = request.POST.get("symptom", None)
    start = request.POST.get("start", None)
    end = request.POST.get("end", None)
    intensity = request.POST.get("intensity", None)
    location = request.POST.get("location", None)
    comments = request.POST.get("comments", None)
    # Create a new symptom entry
    s = Symptoms(user_id=uid, control_id=uid, symptom=symptom, start=start, end=end, intensity=intensity, location=location, comments=comments)
    s.save()
    # Send response
    template = loader.get_template('dashboard/message.html')
    context = {"message": "Your new symptom was successfully added to the database."}
    return HttpResponse(template.render(context, request))

def new_password(request):
    # Get form input
    old_pass = request.POST.get("old_password", None)
    new_pass = request.POST.get("new_password", None)

    # Check that the user is authenticated first
    u = request.user
    if not u.is_authenticated() or not u == authenticate(username=request.user.username, password=old_pass):
        template = loader.get_template('dashboard/message.html')
        return HttpResponse(template.render({"message":"Your current password is incorrect."}, request))

    # Change the password
    u.set_password(new_pass)
    u.save()

    # Send response
    template = loader.get_template('dashboard/message.html')
    context = {"message": "Your password has been changed successfully!"}
    return HttpResponse(template.render(context, request))
