from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
def CSP(request):
    # Check user is logged in
    if not request.user.is_authenticated:
        # Redirect user if not logged in
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, 'customer-service-portal.html')