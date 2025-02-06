from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_template_loads_correct_recipe(self):
        title_test = 'This is a detail page - only one page'

        self.make_recipe(title=title_test)

        response = self.client.get(reverse('recipes:recipe_detail', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(title_test, content)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(reverse('recipes:recipe_detail', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_returns_404_not_found_recipe(self):
        response = self.client.get(
            reverse('recipes:recipe_detail', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_details_template_not_loads_not_published(self):
        """ test recipe is_published False dont show
        """

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe_detail', kwargs={'id': recipe.id})
        )

        self.assertEqual(response.status_code, 404)
