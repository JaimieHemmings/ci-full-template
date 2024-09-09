from django.contrib import admin

# Register your models here.
from home.models import Category, Comment, Post
from portfolio.models import Portfolio

class CategoryAdmin(admin.ModelAdmin):
  pass

class PostAdmin(admin.ModelAdmin):
  pass

class CommentAdmin(admin.ModelAdmin):
  pass

class PortfolioAdmin(admin.ModelAdmin):
  pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

