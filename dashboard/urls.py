from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^settings$', views.settings), 
]
