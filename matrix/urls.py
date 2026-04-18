from django.urls import path
from . import views

app_name = 'matrix'


urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('article/<int:article_id>', views.article_view, name='article_view')
]