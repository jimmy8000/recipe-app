# Generated by Django 5.0.6 on 2024-05-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
