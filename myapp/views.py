from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import ArticleModel
from django.db.models import Q

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def form_view(request):
    submitted = False
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        author = request.POST.get('author')
        date = request.POST.get('date')
        ArticleModel.objects.create(
            title=title,
            description = desc,
            author = author,
            date = date,
        )
        submitted = True
    return render(request, 'form.html', {'submitted': submitted})

def articles_view(request):
    articles = ArticleModel.objects.all()
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__icontains=query)
        )
    return render(request, 'articles.html', {'articles': articles})

def update_view(request, id):
    articles = get_object_or_404(ArticleModel, id=id)
    if request.method == 'POST':
        articles.title = request.POST.get('title')
        articles.description = request.POST.get('description')
        articles.author = request.POST.get('author')
        articles.date = request.POST.get('date')
        articles.save()
        return redirect('articles')
    return render(request, 'update.html', {'articles': articles})


def delete_view(request, id):
    articles = get_object_or_404(ArticleModel, id=id)
    if request.method == 'POST':
        articles.delete()
        return redirect('articles')
    return render(request, 'delete.html', {'articles': articles})

