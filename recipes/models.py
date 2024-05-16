from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=10, editable=False)
    instructions = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    
    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)

    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(',')
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            return 'easy'
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            return 'medium'
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            return 'intermediate'
        else:
            return 'hard'

    def __str__(self):
        return self.name
    