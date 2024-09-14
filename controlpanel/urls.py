from django.urls import path
from . import views

urlpatterns = [
  # Root URL
  path('',
       views.ControlPanel,
       name='control_panel'),

  # URLs for Message Management
  path('messages/',
       views.Messages,
       name='messages'),
  path('messages/read_message/<int:message_id>/',
       views.ReadMessage,
       name='read_message'),
  path('messages/delete_message/<int:message_id>/',
       views.DeleteMessage,
       name='delete_message'),

  # URLs For Project Management
  path('project_admin',
       views.projectAdmin,
       name='project_admin'),
  path('project_view/<int:project_id>/',
       views.ProjectView,
       name='project_view'),

  # URLs for Blog Management
  path('article_view/',
       views.ArticleView,
       name='article_view'),
  path('article_view/delete_blog_confirm/<int:blog_id>/',
       views.DeleteArticleConfirm,
       name='delete_blog_confirm'),
  path('article_view/delete_article/<int:blog_id>/',
       views.DeleteArticle,
       name='delete_article'),
  path('create_article/',
       views.CreateArticle,
       name='create_article'),
  path('edit_article/<int:blog_id>/',
       views.EditArticle,
       name='edit_article'),

  # URLs for Portfolio Management
  path('portfolio_management/',
       views.PortfolioManagement,
       name='portfolio_management'),
  path('portfolio_management/delete_portfolio_confirm/<int:portfolio_id>/',
       views.DeletePortfolioConfirm,
       name='delete_portfolio_confirm'),
  path('portfolio_management/delete_portfolio/<int:portfolio_id>/',
       views.DeletePortfolio,
       name='delete_portfolio'),
  path('portfolio_management/create_portfolio/',
       views.CreatePortfolio,
       name='create_portfolio'),
  path('edit_portfolio/<int:portfolio_id>/',
       views.EditPortfolio,
       name='edit_portfolio'),
]
