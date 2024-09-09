from django.shortcuts import render
from .models import Portfolio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def portfolio(request):
    """
    A view to return portfolio page
    """

    items = Portfolio.objects.all().order_by('-created_on')
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
        page = 1


    return render(request,
                  'portfolio.html',
                  {'page_obj': page_obj,
                   'items': items,
                   'paginator': paginator},)