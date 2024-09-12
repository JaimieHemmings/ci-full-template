from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import Message, Post
from CSP.models import Project, ProjectMessage
from CSP.forms import ProjectFeedbackForm
from django.contrib.auth.decorators import login_required


@login_required
def ControlPanel(request):
    """
    A view to return controlpanel page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    context = {}
    # Get length of unread messages
    unread_messages = Message.objects.filter(read=False).count()
    context['unread_messages'] = unread_messages

    return render(request, 'control-panel.html', context)


@login_required
def Messages(request):
    """
    A view to return messages page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    messages = Message.objects.all().order_by('-created_on')
    context = {
        'messages': messages,
    }

    return render(request, 'messages.html', context)


@login_required
def ReadMessage(request, message_id):
    """
    A view to mark message as read
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    message = Message.objects.get(id=message_id)
    if message.read is True:
        message.read = False
    else:
        message.read = True
    message.save()

    return redirect('messages')


@login_required
def DeleteMessage(request, message_id):
    """
    A view to delete message
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    message = Message.objects.get(id=message_id)
    message.delete()

    return redirect('messages')


@login_required
def projectAdmin(request):
    """
    A view to return project admin page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    projects = Project.objects.all().order_by('-created_on')
    context = {
        'projects': projects,
    }

    return render(request, 'projects-admin.html', context)


@login_required
def ProjectView(request, project_id):
    """
    A view to return project view page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    comments = ProjectMessage.objects.filter(project_id=project_id)
    project = Project.objects.get(id=project_id)
    form = ProjectFeedbackForm()

    context = {
        'project': project,
        'comments': comments,
        'form': form,
    }

    if request.method == 'POST':
        form = ProjectFeedbackForm(request.POST)
        if form.is_valid():
            username = request.user.username
            message = form.cleaned_data['message']
            data = ProjectMessage(project_id=project, name=username, message=message)
            data.save()
            return redirect('project_view', project_id)

    return render(request, 'project-view.html', context)

@login_required
def BlogView(request):
    """
    A view to return blog view page
    """

    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))
    
    context = {}
    blogPosts = Post.objects.all().order_by('-created_on')
    context = {
        'blogPosts': blogPosts,
    }
    
    return render(request, 'blog-view.html', context)


@login_required
def DeleteBlogConfirm(request, blog_id):
    """
    A view to confirm article deletion
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    blog = Post.objects.get(id=blog_id)
    # blog.delete()
    context = {
       'blog': blog,
    }

    return render(request, 'delete-blog-confirm.html', context)
