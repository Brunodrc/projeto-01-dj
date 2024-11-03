from django.test import TestCase
from recipes.utils.recipes.factory_recipe import make_recipe
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        faker = make_recipe()
        category_test = Category.objects.create(name=faker['category']['name'])
        author_test = User.objects.create_user(
            first_name=faker['author']['first_name'],
            last_name=faker['author']['last_name'],
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category_test,
            author=author_test,
            title='titulo da recipe',
            description=faker['description'],
            slug='recipe-slug',
            preparation_time=faker['preparation_time'],
            preparation_time_unit='Minutos',
            servings=faker['servings'],
            servings_unit='Porção',
            preparation_steps=faker['preparation_steps'],
            preparation_steps_is_html=False,
            is_published=True,
        )
        return super().setUp()
