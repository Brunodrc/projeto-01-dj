from django.test import TestCase
from django.urls import reverse


class RecipeURLTest(TestCase):
    def test_the_pytest_is_ok(self):
        ...

    def test_recipe_home_url_is_correct(self):
        recipe_home_url = reverse('recipes:home')
        self.assertEqual(recipe_home_url, '/')
