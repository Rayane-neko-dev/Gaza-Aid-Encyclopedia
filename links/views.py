
from django.http import HttpResponse
from .models import Link
from django.shortcuts import render, get_object_or_404

def Link_view(request):
    links = Link.objects.all()
    return render(request, 'links/links.html', 
    {'links':links} )

