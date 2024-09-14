from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.models import Post, Comment, Message
from portfolio.models import Portfolio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm


# Create your views here.
def index(request):
    """
    A view to return index page
    """
    context = {}
    # Get 3 latest blog Posts
    blog_posts = Post.objects.all().order_by('-created_on')[:3]
    context['blog_posts'] = blog_posts
    # Get 4 latest Portfolio Posts
    portfolio_posts = Portfolio.objects.all().order_by('-created_on')[:4]
    context['portfolio_posts'] = portfolio_posts
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
    context = {}
    # Get 3 latest blog Posts
    blog_posts = Post.objects.all().order_by('-created_on')[:3]
    context['blog_posts'] = blog_posts
    return render(request, 'home/services.html', context)


def blog(request):
    """
    A view to return blog page
    """
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
        page = 1
    return render(request,
                  'home/blog.html',
                  {'page_obj': page_obj,
                   'posts': posts,
                   'paginator': paginator},)


def article(request, slug):
    """
    A view to return article page
    """
    post = Post.objects.get(slug=slug)
    # Get the post ID and grab all the comments related to it
    post_id = post.id
    comments = Comment.objects.filter(post=post_id)
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'home/article.html', context)


def contact(request):
    """
    A view to return contact page
    """
    context = {}
    form = ContactForm()
    context['form'] = form

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            data = Message(name=name, email=email, message=message)
            data.save()
            return HttpResponseRedirect('/contact/message-success/')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', context)


def message_success(request):
    """
    A view to return message success page
    """
    return render(request, 'home/message-success.html')
