from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name_a='Category'):
        return Category.objects.create(name=name_a)

    def make_author(
        self,
        first_name_a='user',
        last_name_a='name',
        username_a='username',
        password_a='123456',
        email_a='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name_a,
            last_name=last_name_a,
            username=username_a,
            password=password_a,
            email=email_a,
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
        title='titulo da recipe',
        description="descrição da receita",
        slug='titulo-da-recipe',
        preparation_time=10,
        preparation_time_unit='Minutos',
        servings=5,
        servings_unit='Porção(ões)',
        preparation_steps='passo a passo para preparar a receita',
        preparation_steps_is_html=False,
        is_published=True,
    ):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            # ** serve para desenpacotar os dados do discionario.
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
