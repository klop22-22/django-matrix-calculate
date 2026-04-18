from django.shortcuts import render, get_object_or_404
from matrix.models import Article, Example
from .matrix_engine import Matrix


def index(request):
    rows_a = int(request.GET.get('rows_a', 4))
    cols_a = int(request.GET.get('cols_a', 5))
    rows_b = int(request.GET.get('rows_b', 4))
    cols_b = int(request.GET.get('cols_b', 5))
    
    rows_a = min(max(rows_a, 1), 6)
    cols_a = min(max(cols_a, 1), 6)
    rows_b = min(max(rows_b, 1), 6)
    cols_b = min(max(cols_b, 1), 6)

    B_view = False
    operation_with_B = ('add', 'sub', 'multiply')

    if request.method == 'POST':
        operation = request.POST.get('operation')
    else:
        operation = request.GET.get('operation')

    if operation in operation_with_B:
        B_view = True

    if request.method == 'POST':
        matrix_a = []
        for i in range(rows_a):
            row = []
            for j in range(cols_a):
                val = request.POST.get(f'cell_a_{i}_{j}', '0')
                row.append(float(val) if val else 0)
            matrix_a.append(row)
        
        if operation in operation_with_B:
            matrix_b = []
            for i in range(rows_b):
                row = []
                for j in range(cols_b):
                    val = request.POST.get(f'cell_b_{i}_{j}', '0')
                    row.append(float(val) if val else 0)
                matrix_b.append(row)   

        result = None
        error = None
        
        try:
            mat_a = Matrix(matrix_a)
            
            if operation == 'add':
                mat_b = Matrix(matrix_b)
                result = mat_a.add(mat_b).matrix
            elif operation == 'sub':
                mat_b = Matrix(matrix_b)
                result = mat_a.sub(mat_b).matrix
            elif operation == 'multiply':
                mat_b = Matrix(matrix_b)
                result = mat_a.multiply(mat_b).matrix
            elif operation == 'determinant':
                result = mat_a.determinant()
        except ValueError as e:
            error = str(e)        
        
        context = {
            'rows_a': range(rows_a),
            'columns_a': range(cols_a),
            'rows_b': range(rows_b),
            'columns_b': range(cols_b),
            'B_view': B_view,
            'operation': operation,
            'result_matrix': result,
            'error': error,
        }
        print(f"RESULT: {result}")
        print(f"ERROR: {error}")
        return render(request, 'matrix/index.html', context)
    
    context = {
        'rows_a': range(rows_a),
        'columns_a': range(cols_a),
        'rows_b': range(rows_b),
        'columns_b': range(cols_b),
        'B_view': B_view,
        'operation': operation,
    }
    return render(request, 'matrix/index.html', context)


def article(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'matrix/articles.html', context)


def article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    examples = Example.objects.filter(category=article)
    context = {
        'article': article,
        'examples': examples,
    }
    return render(request, 'matrix/article_view.html', context)