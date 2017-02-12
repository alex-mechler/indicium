from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^settings$', views.settings, name="settings"),
    url(r'^changesettings$', views.post_settings, name="post_settings"),
    url(r'^changepass$', views.post_password, name="post_password"),
	url(r'^post_symptom$', views.post_symptom, name="post_symptom"),
    url(r'^newsymptom$', views.new_symptom, name="new_symptom"),
    url(r'^$', views.index, name="index"),
]
