from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
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

    chart = None
    if not df.empty:
        chart_type = request.GET.get('chart_type')
        if chart_type:
            chart = get_chart(chart_type, df, labels=df['difficulty'].unique() if 'difficulty' in df.columns else [])

    return render(request, 'recipe_list.html', {'form': form, 'table_html': table_html, 'recipes': recipes, 'chart': chart})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    instructions = recipe.instructions.split(';') if recipe.instructions else []
    instructions = [instr.strip() for instr in instructions if instr.strip()]  
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'instructions': instructions})