from django.shortcuts import render, redirect
from django.conf import settings
from .models import Project

# Create your views here.
def CSP(request):
    # Check user is logged in
    if not request.user.is_authenticated:
        # Redirect user if not logged in
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    # Get the current users username
    username = request.user.username

    # Get all projects owned by user
    projects = Project.objects.filter(owner=username)

    return render(request, 'customer-service-portal.html', {'projects': projects})