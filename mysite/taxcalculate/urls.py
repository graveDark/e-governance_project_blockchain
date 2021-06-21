from django.urls import path
from . import views

urlpatterns = [
    path('user', views.index, name='Index'),
    path('register', views.createNewUser, name='Register'),
    path('user_submit', views.index_submit, name='Index Submit'),
    path('register_submit', views.createNewUser_submit, name='Register Submit'),
    path('profile', views.login, name='Profile')
]