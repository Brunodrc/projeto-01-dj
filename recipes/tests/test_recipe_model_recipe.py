from django.core.exceptions import ValidationError
from .test_recipe_base import RecipeTestBase, Recipe
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'B' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def make_recipe_no_defalts(self):
        recipe = Recipe(
            category=self.make_category(name_a='test default'),
            author=self.make_author(username_a='testusername'),
            title='titulo da recipe',
            description="descrição da receita",
            slug='titulo-da-recipe',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porção(ões)',
            preparation_steps='passo a passo para preparar a receita',
        )

        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_preparation_steps_is_html_default_false(self):
        recipe = self.make_recipe_no_defalts()
        self.assertFalse(recipe.preparation_steps_is_html,
                         msg='Recipe preparation_steps_is_html is not False.'
                         )

    def test_recipe_is_published_default_false(self):
        recipe = self.make_recipe_no_defalts()
        self.assertFalse(recipe.is_published,
                         msg='Recipe is_published is not False.'
                         )

# def test_recipe_title_raise_error_if_title_more_than_65_char(self):
    #     self.recipe.title = 'B' * 66

    #     with self.assertRaises(ValidationError):
    #         self.recipe.full_clean()
    # será usado um teste parametrizado para analisar individualmente cada
    # parte do teste que está colocado dentro de um unico teste
