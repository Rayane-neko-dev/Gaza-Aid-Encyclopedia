from django.db import models
from cloudinary.models import CloudinaryField
# listings/models.py

class Link(models.Model):
    link_id = models.fields.IntegerField()
    image = CloudinaryField('image', blank=True, null=True)
    title = models.fields.CharField(max_length=100)
    content = models.fields.CharField(max_length=1000)
    date = models.fields.DateField()
    link = models.URLField(max_length=500)

    def __str__(self):
     return f'{self.title}'
