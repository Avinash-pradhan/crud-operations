from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title

