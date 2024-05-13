from django.test import TestCase
from .models import Recipe
# Create your tests here.

class RecipeModelTest(TestCase):
    def setUp(self):
        Recipe.objects.create(name='Test Recipe', ingredients='Test Ingredients', cooking_time=5)
    
    def test_recipe_name(self):
        recipe = Recipe.objects.get(name='Test Recipe')
        self.assertEqual(recipe.name, 'Test Recipe')
    
    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(name='Test Recipe')
        self.assertEqual(recipe.ingredients, 'Test Ingredients')
    
    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(name='Test Recipe')
        self.assertEqual(recipe.cooking_time, 5)