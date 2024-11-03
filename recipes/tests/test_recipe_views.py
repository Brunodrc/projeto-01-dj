from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase, Recipe


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
        Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Sem receitas publicadas ainda!',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
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
        self.assertIn('Minutos', content)
        self.assertIn('Porção', content)

        # se contém a receita enviada
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'id_category': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_returns_404_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'id_category': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(reverse('recipes:recipe_detail', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_returns_404_not_found_recipe(self):
        response = self.client.get(
            reverse('recipes:recipe_detail', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
