from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/submit_login/', views.submit_login, name='submit_login'),
]