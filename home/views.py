from django.shortcuts import render
from home.models import Post, Comment

# Create your views here.

def index(request):
    """
    A view to return index page
    """
    """ Get 3 latest blog Posts"""
    posts = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'posts': posts,
    }
    return render(request, 'home/index.html', context)

def about(request):
    """
    A view to return about page
    """
    return render(request, 'home/about.html')

def services(request):
    """
    A view to return services page
    """
    return render(request, 'home/services.html')

def contact(request):
    """
    A view to return contact page
    """
    return render(request, 'home/contact.html')
