from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^settings$', views.settings, name="settings"),
    url(r'^newpassword$', views.new_password, name="new_password"),
    url(r'^dependants$', views.index, name='dependants'),
    url(r'^newsymptom$', views.new_symptom, name="new_symptom"),
    url(r'^$', views.index, name="index"),
]
