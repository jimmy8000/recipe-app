from django.urls import reverse
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
    
    def test_calculate_difficulty(self):
        recipe = Recipe(
            name="Test Recipe",
            ingredients="ingredient1, ingredient2, ingredient3",
            cooking_time=4
        )
        recipe.save()
        self.assertEqual(recipe.difficulty, 'easy')
        
class RecipeViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="ingredient1, ingredient2",
            cooking_time=10,
            instructions="Step 1; Step 2",
            difficulty="easy"
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_list.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')