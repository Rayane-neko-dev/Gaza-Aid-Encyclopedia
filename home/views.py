from django.shortcuts import render
from articles.models import Article
from links.models import Link

def home(request):
 articles = Article.objects.all()
 links = Link.objects.all()
 context = {'articles': articles ,'links' : links }
 return render(request, 'home/home.html', context)