from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(code=200)

def article(request, article_id):
    try:
        resolved_article = Item.objects.get(id=article_id)
    except Item.objects.model.DoesNotExist:
        return HttpResponse(code=404)
    return render(request, "templates/article", context={'article': resolved_article,
                                                         'pubdate': resolved_article.pub_date.strftime("%B %Y")})
