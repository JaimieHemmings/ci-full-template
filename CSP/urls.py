from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.CSP, name='csp'),
  path('project/<int:project_id>/', views.project, name='project'),
]