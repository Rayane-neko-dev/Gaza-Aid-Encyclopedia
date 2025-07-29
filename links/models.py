from django.db import models

# listings/models.py

class Link(models.Model):
    link_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/links', null=True, blank=True)
    title = models.fields.CharField(max_length=100)
    content = models.fields.CharField(max_length=1000)
    date = models.fields.DateField()

    def __str__(self):
     return f'{self.title}'