from django.shortcuts import render, redirect
from home.models import Message, Post
from CSP.models import Project, ProjectMessage
from CSP.forms import ProjectFeedbackForm
from portfolio.models import Portfolio
from .forms import CreateArticleForm, CreatePortfolioForm
from django.contrib import messages
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def ControlPanel(request):
    """
    A view to return controlpanel page
    """
    context = {}
    # Get length of unread messages
    unread_messages = Message.objects.filter(read=False).count()
    context['unread_messages'] = unread_messages

    return render(request, 'control-panel.html', context)


@user_passes_test(lambda u: u.is_superuser)
def Messages(request):
    """
    A view to return messages page
    """
    messages = Message.objects.all().order_by('-created_on')
    context = {
        'messageEntries': messages,
    }

    return render(request, 'messages/messages.html', context)


@user_passes_test(lambda u: u.is_superuser)
def ReadMessage(request, message_id):
    """
    A view to mark message as read
    """
    message = Message.objects.get(id=message_id)
    if message.read is True:
        message.read = False
        messages.success(request, 'Message marked as unread')
    else:
        message.read = True
        messages.success(request, 'Message marked as read')
    message.save()

    return redirect('messages')


@user_passes_test(lambda u: u.is_superuser)
def DeleteMessage(request, message_id):
    """
    A view to delete message
    """

    message = Message.objects.get(id=message_id)
    message.delete()
    # flash notification message
    messages.success(request, 'Message Deleted')

    return redirect('messages')


@user_passes_test(lambda u: u.is_superuser)
def projectAdmin(request):
    """
    A view to return project admin page
    """

    projects = Project.objects.all().order_by('-created_on')
    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects-admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def ProjectView(request, project_id):
    """
    A view to return project view page
    """

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
            data = ProjectMessage(
                project_id=project,
                name=username,
                message=message
                )
            data.save()
            return redirect('project_view', project_id)

    return render(request, 'projects/project-view.html', context)


@user_passes_test(lambda u: u.is_superuser)
def ArticleView(request):
    """
    A view to return blog view page
    """
    context = {}
    blogPosts = Post.objects.all().order_by('-created_on')
    context = {
        'blogPosts': blogPosts,
    }

    return render(request, 'blog/article-view.html', context)


@user_passes_test(lambda u: u.is_superuser)
def DeleteArticleConfirm(request, blog_id):
    """
    A view to confirm article deletion
    """

    blog = Post.objects.get(id=blog_id)
    context = {
       'blog': blog,
    }

    return render(request, 'blog/delete-article-confirm.html', context)


@user_passes_test(lambda u: u.is_superuser)
def DeleteArticle(request, blog_id):
    """
    A view to delete article
    """
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    # flash notification message
    messages.success(request, 'Article Deleted')

    return redirect('article_view')


@user_passes_test(lambda u: u.is_superuser)
def CreateArticle(request):
    """
    A view to create article
    """
    context = {}
    form = CreateArticleForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # Create the slug from the title
            form.instance.slug = slugify(form.instance.title)
            form.instance.created_by = request.user.username
            form.instance.modified_by = request.user.username
            form.save()
            # flash notification message
            messages.success(request, 'Article Created')
            return redirect('article_view')
        else:
            context['field_errors'] = form.errors
            messages.error(
                request,
                "The form data wasn't able to be saved. Please try again."
                )

    context['form'] = form
    return render(request, 'blog/create-article.html', context)


@user_passes_test(lambda u: u.is_superuser)
def EditArticle(request, blog_id):
    """
    A view to edit an article.
    """

    context = {}
    # Retrieve the blog post by ID
    blog = Post.objects.get(id=blog_id)
    # Instantiate the form with the existing blog instance
    form = CreateArticleForm(instance=blog)

    if request.method == 'POST':
        # Re-instantiate the form with POST data and the existing blog instance
        form = CreateArticleForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            # Update additional fields not in the form
            form.instance.modified_by = request.user.username
            form.instance.modified_on = timezone.now()
            form.instance.slug = slugify(form.instance.title)
            # Save the form, which updates the existing blog instance
            form.save()
            # Flash a success notification message
            messages.success(request, 'Article Edited')
            return redirect('article_view')
        else:
            # If the form is not valid, add form errors to the context
            context['field_errors'] = form.errors
            messages.error(
                request,
                "The form data wasn't able to be saved. Please try again."
            )

    # Add the form to the context
    context['form'] = form
    context['article_id'] = blog_id
    return render(request, 'blog/edit-article.html', context)


@user_passes_test(lambda u: u.is_superuser)
def PortfolioManagement(request):
    """
    A view to return portfolio management page
    """
    portfolioItems = Portfolio.objects.all().order_by('-created_on')
    context = {}
    context['portfolioItems'] = portfolioItems

    return render(request, 'portfolio/portfolio-management.html', context)


@user_passes_test(lambda u: u.is_superuser)
def DeletePortfolioConfirm(request, portfolio_id):
    """
    A view to confirm portfolio deletion
    """
    portfolio = Portfolio.objects.get(id=portfolio_id)
    context = {
       'portfolio': portfolio,
    }

    return render(request, 'portfolio/delete-portfolio-confirm.html', context)


@user_passes_test(lambda u: u.is_superuser)
def DeletePortfolio(request, portfolio_id):
    """
    A view to delete portfolio
    """
    portfolio = Portfolio.objects.get(id=portfolio_id)
    portfolio.delete()
    # flash notification message
    messages.success(request, 'Portfolio Deleted')

    return redirect('portfolio_management')


@user_passes_test(lambda u: u.is_superuser)
def CreatePortfolio(request):
    """
    A view to create portfolio
    """
    context = {}
    form = CreatePortfolioForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # Create the slug from the title
            form.instance.slug = slugify(form.instance.title)
            form.instance.created_by = request.user.username
            form.instance.modified_by = request.user.username
            form.save()
            # flash notification message
            messages.success(request, 'Portfolio Created')
            return redirect('portfolio_management')
        else:
            context['field_errors'] = form.errors
            messages.error(
                request,
                "The form data wasn't able to be saved. Please try again."
                )
        return redirect('portfolio_management')

    context['form'] = form
    return render(request, 'portfolio/create-portfolio.html', context)


@user_passes_test(lambda u: u.is_superuser)
def EditPortfolio(request, portfolio_id):
    """
    A view to edit a portfolio.
    """

    context = {}
    # Retrieve the portfolio item by ID
    portfolio = Portfolio.objects.get(id=portfolio_id)
    # Instantiate the form with the existing portfolio instance
    form = CreatePortfolioForm(instance=portfolio)

    if request.method == 'POST':
        # Re-instantiate the form with POST data and the existing portfolio instance
        form = CreatePortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            # Update additional fields not in the form
            form.instance.modified_by = request.user.username
            form.instance.modified_on = timezone.now()
            form.instance.slug = slugify(form.instance.title)
            # Save the form, which updates the existing portfolio instance
            form.save()
            # Flash a success notification message
            messages.success(request, 'Portfolio Edited')
            return redirect('portfolio_management')
        else:
            # If the form is not valid, add form errors to the context
            context['field_errors'] = form.errors
            messages.error(
                request,
                "The form data wasn't able to be saved. Please try again."
            )

    # Add the form to the context
    context['form'] = form
    context['portfolio_id'] = portfolio_id
    return render(request, 'portfolio/edit-portfolio.html', context)