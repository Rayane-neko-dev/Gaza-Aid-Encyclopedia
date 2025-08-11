from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator

# Create your models here.

class Article(models.Model):
    article_id = models.fields.IntegerField()
    image = CloudinaryField('image', blank=True, null=True)
    title = models.fields.CharField(max_length=100)
    content = models.TextField(validators=[MaxLengthValidator(100000)])
    date = models.fields.DateField()

    def __str__(self):
     return f'{self.title}'
