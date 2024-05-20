from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.welcome, name='welcome'),  
    path('recipes/', views.recipe_list, name='recipe_list'), 
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]