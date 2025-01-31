from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    def test_recipe_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_returns_template_correct(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_show_not_fund_recipes(self):

        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Sem receitas publicadas ainda!',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        # testar o contexto de fora para dentro, ou seja,
        # verificando se o contexto enviado foi o que está salvo
        response = self.client.get(reverse('recipes:home'))
        # aqui testa se a receita está sendo exibida na tela
        # response_recipes = response.context['recipes']
        # self.assertEqual(response_recipes.first().title, 'titulo da recipe')
        # testar se o contexto está correto
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        # carrega o título e outras partes da receita
        self.assertIn('titulo da recipe', content)

        # se contém a receita enviada
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_not_loads_not_published(self):
        """ test recipe is_published False dont show
        """

        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'Sem receitas publicadas ainda!',
            response.content.decode('utf-8')
        )

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

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)
