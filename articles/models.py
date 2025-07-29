from django.db import models

# Create your models here.

class Article(models.Model):
    article_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/article', null=True, blank=True)
    title = models.fields.CharField(max_length=100)
    content = models.fields.CharField(max_length=1000)
    date = models.fields.DateField()

    def __str__(self):
     return f'{self.title}'