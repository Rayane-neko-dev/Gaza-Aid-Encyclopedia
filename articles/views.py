
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404

def article_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', 
    {'articles':articles} )



def article_detailed_view(request, article_id):
    article = get_object_or_404(Article, article_id=article_id)
    return render(request, 'articles/article_detailed.html', {'article': article} )