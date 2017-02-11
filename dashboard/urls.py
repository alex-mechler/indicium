from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'dashboard'
urlpatterns = [
#     url(r'^/settings(?P<question_id>[0-9]+)/vote/$'
    url(r'^settings$', views.settings), 
]
