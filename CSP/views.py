from django.shortcuts import render, redirect
from django.conf import settings
from .models import Project, ProjectMessage
from .forms import ProjectFeedbackForm
from django.contrib.auth.decorators import login_required


@login_required
def CSP(request):
    """ Customer Service Portal view """    
    # Get the current users username
    username = request.user.username
    # Get all projects owned by user
    projects = Project.objects.filter(owner=username)
    return render(request, 'customer-service-portal.html', {'projects': projects})


@login_required
def project(request, project_id):
    """ Project view """    
    context = {}
    # Get the project with the given id
    project = Project.objects.get(id=project_id)
    form = ProjectFeedbackForm()
    # Get all comments for the project
    comments = ProjectMessage.objects.filter(project_id=project_id)
    context['comments'] = comments
    context['form'] = form
    context['project'] = project

    if request.method == 'POST':
        form = ProjectFeedbackForm(request.POST)
        if form.is_valid():
            username = request.user.username
            message = form.cleaned_data['message']
            data = ProjectMessage(project_id=project, name=username, message=message)
            data.save()
            return redirect('project', project_id)

    
    return render(request, 'project.html', context)