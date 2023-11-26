
from django.contrib import admin
from django.urls import path

from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('profile/', views.login)
]
