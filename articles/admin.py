from django.contrib import admin

from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):

 list_display = ('title','date','image') 

admin.site.register(Article, ArticleAdmin)