from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_template_loads_category(self):
        title_test = 'This is a category test'

        self.make_recipe(title=title_test)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(title_test, content)

    def test_recipe_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'id_category': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_returns_404_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'id_category': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_not_loads_not_published(self):
        """ test recipe is_published False dont show
        """

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:category', kwargs={
                    'id_category': recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)
