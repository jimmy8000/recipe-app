from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, RecipeForm
import pandas as pd
from .utils import get_chart

def welcome(request):
    return render(request, 'welcome.html')

@login_required
def recipe_list(request):
    form = RecipeSearchForm(request.GET or None)
    
    recipes = Recipe.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            recipes = recipes.filter(name__icontains=query)

    df = pd.DataFrame(list(recipes.values()))
    table_html = df.to_html(classes='table table-striped') if not df.empty else "No data available"

    return render(request, 'recipe_list.html', {'form': form, 'table_html': table_html, 'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    instructions = recipe.instructions.split(';') if recipe.instructions else []
    instructions = [instr.strip() for instr in instructions if instr.strip()]  
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'instructions': instructions})

@login_required
def statistics(request):
    chart = None
    form = RecipeSearchForm(request.GET or None)

    if form.is_valid():
        chart_type = form.cleaned_data.get('chart_type')

        # Querying the Recipe model to get actual data
        recipes = Recipe.objects.all()

        # Convert the queried data to a DataFrame
        data = {
            'difficulty': [recipe.difficulty for recipe in recipes],
            'cooking_time': [recipe.cooking_time for recipe in recipes]
        }

        df = pd.DataFrame(data)

        labels = df['difficulty'].value_counts().index.tolist() if chart_type == '#2' else None

        chart = get_chart(chart_type, df, labels=labels)

    return render(request, 'statistics.html', {'form': form, 'chart': chart})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_list')  # Redirect to the recipe list after saving
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

def about_me(request):
    return render(request, 'about_me.html')