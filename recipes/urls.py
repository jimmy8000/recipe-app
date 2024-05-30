from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.welcome, name='welcome'),  
    path('recipes/', views.recipe_list, name='recipe_list'), 
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
    path('recipes/statistics/', views.statistics, name='statistics'),
    path('about/', views.about_me, name='about_me'),
]