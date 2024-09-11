from django.urls import path
from . import views

urlpatterns = [
  path('', views.ControlPanel, name='controlpanel'),
  path('messages/', views.Messages, name='messages'),
  path('read_message/<int:message_id>/', views.ReadMessage, name='read_message'),
  path('delete_message/<int:message_id>/', views.DeleteMessage, name='delete_message'),
  path('project_admin', views.project_admin, name='project_admin'),
  path('project_view/<int:project_id>/', views.project_view, name='project_view'),
]