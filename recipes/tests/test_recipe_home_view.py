from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

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
