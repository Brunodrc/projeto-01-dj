from django.test import TestCase
from django.urls import reverse


class RecipeURLTest(TestCase):
    def test_the_pytest_is_ok(self):
        ...

    def test_recipe_home_url_is_correct(self):
        recipe_home_url = reverse('recipes:home')
        self.assertEqual(recipe_home_url, '/')

    def test_recipe_category_url_is_correct(self):
        recipe_category_url = reverse(
            'recipes:category', kwargs={'id_category': 1})
        self.assertEqual(recipe_category_url, '/recipes/category/1/')

    def test_recipe_recipe_detail_url_is_correct(self):
        recipe_recipe_detail_url = reverse(
            'recipes:recipe_detail', kwargs={'id': 1})
        self.assertEqual(recipe_recipe_detail_url, '/recipes/1/')

    """  criando uma url a partir do TDD - 
        primeiro criase o teste para falhar
        segundo corrige o erro do teste
        terceiro refatora o código 
    """

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search')
