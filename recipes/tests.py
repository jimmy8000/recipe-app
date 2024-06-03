from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeSearchForm, RecipeForm

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
        
class RecipeViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="ingredient1, ingredient2",
            cooking_time=10,
            instructions="Step 1; Step 2",
            difficulty="easy"
        )
    
    def setUp(self):
        self.client = Client()
    
    def test_recipe_list_view_login_required(self):
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertRedirects(response, '/login/?next=/recipes/')
    
    def test_recipe_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_list.html')
        self.assertContains(response, "Test Recipe")
    
    def test_recipe_list_view_empty(self):
        Recipe.objects.all().delete()
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available")
    
    def test_recipe_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertContains(response, "Test Recipe")
        self.assertContains(response, "Step 1")
    
    def test_add_recipe_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('recipes:add_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')
    
    def test_add_recipe_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('recipes:add_recipe'), {
            'name': 'New Recipe',
            'ingredients': 'ingredient1, ingredient2',
            'cooking_time': 15,
            'instructions': 'Step 1; Step 2',
            'difficulty': 'easy'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Recipe.objects.filter(name='New Recipe').exists())
        
class RecipeFormTest(TestCase):
    def test_recipe_search_form_valid_data(self):
        form = RecipeSearchForm(data={
            'query': 'Spaghetti',
            'chart_type': '#1'
        })
        self.assertTrue(form.is_valid())
    
    def test_recipe_search_form_no_data(self):
        form = RecipeSearchForm(data={})
        self.assertTrue(form.is_valid())
    
    def test_recipe_search_form_invalid_chart_type(self):
        form = RecipeSearchForm(data={
            'query': 'Spaghetti',
            'chart_type': 'invalid_choice'
        })
        self.assertFalse(form.is_valid())
    
    def test_recipe_form_valid_data(self):
        form = RecipeForm(data={
            'name': 'Test Recipe',
            'ingredients': 'Test Ingredients',
            'cooking_time': 10,
            'instructions': 'Step 1; Step 2',
            'difficulty': 'easy'
        })
        self.assertTrue(form.is_valid())
    
    def test_recipe_form_invalid_data(self):
        form = RecipeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  