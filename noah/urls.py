from django.urls import path
from . import views

app_name = 'noah'

urlpatterns = [
    path('login/', views.LoginView, name='login')
]