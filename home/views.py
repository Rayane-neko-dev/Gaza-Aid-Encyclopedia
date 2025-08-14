from django.shortcuts import render
from links.models import Link

def home(request):
 links = Link.objects.all().order_by('-id')[:3]  
 context = {'links' : links }
 return render(request, 'home/home.html', context)
