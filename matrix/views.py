from django.shortcuts import render

from matrix.models import Article

def index(request):
    context = {
        'matrix': 'matrix',
        'rows': range(4),
        'columns': range(5),
    }
    return render(request, 'matrix/index.html', context)

def article(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'matrix/articles.html', context)