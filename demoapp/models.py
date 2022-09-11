from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class news(models.Model):
    date = models.IntegerField()
    pic = models.ImageField(upload_to='picture')
    month = models.TextField()
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
