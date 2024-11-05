# users/urls.py
from django.urls import path
from . import views

app_name = 'users'  # Ensure this is set to 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user, name='user'),  # The user profile URL
    path('logout/', views.logout_view, name='logout'),
]
