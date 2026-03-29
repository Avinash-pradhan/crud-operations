from django.contrib import admin
from myapp.models import ArticleModel
# Register your models here.


@admin.register(ArticleModel)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'date')