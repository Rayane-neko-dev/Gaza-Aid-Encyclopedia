from django.contrib import admin

from links.models import Link

class LinkAdmin(admin.ModelAdmin):

 list_display = ('title','date','image') 

admin.site.register(Link, LinkAdmin)