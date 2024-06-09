from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=100)
    published_date=models.DateField(default=timezone.now)
    class Meta:
        db_table = 'posts'
        ordering=['-published_date']

