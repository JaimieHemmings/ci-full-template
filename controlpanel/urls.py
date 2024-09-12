from django.urls import path
from . import views

urlpatterns = [
  path('', views.ControlPanel, name='control_panel'),
  path('messages/', views.Messages, name='messages'),
  path('read_message/<int:message_id>/', views.ReadMessage, name='read_message'),
  path('delete_message/<int:message_id>/', views.DeleteMessage, name='delete_message'),
  path('project_admin', views.projectAdmin, name='project_admin'),
  path('project_view/<int:project_id>/', views.ProjectView, name='project_view'),
  path('article_view/', views.ArticleView, name='article_view'),
  path('article_view/delete_blog_confirm/<int:blog_id>/', views.DeleteArticleConfirm, name='delete_blog_confirm'),
  path('article_view/delete_article/<int:blog_id>/', views.DeleteArticle, name='delete_article'),
  path('create_article/', views.CreateArticle, name='create_article'),
]