from django.core.exceptions import ValidationError
from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name_a='Category testing')
        return super().setUp()

    def test_category_representation_str(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_category_name_max_length_65_char(self):
        self.category.name = "B" * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
