from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.registration, name = 'signup'),
    url(r'^register', views.register, name = 'register')
]
