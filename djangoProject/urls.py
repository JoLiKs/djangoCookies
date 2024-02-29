
from django.contrib import admin
from django.urls import path

from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('profile/', views.profile),
    path('testo/', views.testo)
]
