from django.shortcuts import render
from home.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'home/article.html', context)


def contact(request):
    """
    A view to return contact page
    """
    return render(request, 'home/contact.html')
