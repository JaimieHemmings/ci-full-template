from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view to return index page
    """
    return render(request, 'home/index.html')

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
