from django.urls import path
from . import views

urlpatterns = [
  path('', views.ControlPanel, name='control_panel'),
  path('messages/', views.Messages, name='messages'),
  path('read_message/<int:message_id>/', views.ReadMessage, name='read_message'),
  path('delete_message/<int:message_id>/', views.DeleteMessage, name='delete_message'),
  path('project_admin', views.projectAdmin, name='project_admin'),
  path('project_view/<int:project_id>/', views.ProjectView, name='project_view'),
  path('blog_view/', views.BlogView, name='blog_view'),
  path('blog_view/delete_blog_confirm/<int:blog_id>/', views.DeleteBlogConfirm, name='delete_blog_confirm'),
]