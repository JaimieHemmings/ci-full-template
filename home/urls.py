from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.article, name='article'),
    path('/portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('contact/message-success/', views.message_success, name='message-success'),
]
