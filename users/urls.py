from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('user_history/', views.user_history, name='user_history')
]