from django.shortcuts import render

def index(request):
    context = {
        'title': 'Matrix',
        'cells': [
            'Cell1',
            'Cell2',
        ]
    }
    return render(request, 'matrix/index.html', context)
