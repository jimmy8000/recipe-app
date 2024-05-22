from django import forms

class RecipeSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Recipe Name')
    CHART_CHOICES = [
        ('#1', 'Bar Chart: Number of Recipes by Difficulty Level'),
        ('#2', 'Pie Chart: Recipe Distribution by Difficulty Level'),
        ('#3', 'Line Chart: Cooking Time of Recipes')
    ]
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False, label='Chart Type')