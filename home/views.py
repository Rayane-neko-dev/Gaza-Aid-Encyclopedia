from django.shortcuts import render
from articles.models import Article
from links.models import Link

def home(request):
 articles = Article.objects.all()
 links = Link.objects.all()
 context = {'articles': articles ,'links' : links }
 return render(request, 'home/home.html', context)

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            # Here you would normally send an email or save the message
            success = True
    return render(request, 'home/contact.html', {'success': success})