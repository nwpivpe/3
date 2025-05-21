from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")
        self.assertEqual(list(iter(category)), ["Desserts"])

class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        category = Category.objects.create(name="Main Dish")
        recipe = Recipe.objects.create(
            title="Pasta",
            description="Delicious pasta recipe",
            instructions="Boil water, cook pasta, add sauce",
            ingredients="Pasta, water, sauce",
            category=category
        )
        self.assertEqual(str(recipe), "Pasta")
        self.assertEqual(recipe.category.name, "Main Dish")
