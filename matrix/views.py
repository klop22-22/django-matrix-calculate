from django.shortcuts import render

def index(request):
    context = {
        'matrix': 'matrix',
        'rows': range(4),
        'columns': range(5),
    }
    return render(request, 'matrix/index.html', context)
