from unittest import TestCase
from .pagination import make_pagination_range
from ..tests.test_recipe_base import RecipeTestBase
from django.urls import response


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa E501
        # pagina atual = 1, quantidade de paginas 2, pagina do meio 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # pagina atual = 2, quantidade de paginas 2, pagina do meio 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # pagina atual = 3, quantidade de paginas 2, pagina do meio 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        # pagina atual = 10, quantidade de paginas 2, pagina do meio 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # pagina atual = 2, quantidade de paginas 2, pagina do meio 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    # def test_show_number_correct_recipe_per_page(self):
    #     total_recipes = []

    #     for x in range(0, 15):
    #         x = RecipeTestBase.make_recipe(title=f'receita-teste{str(x)}',
    #                                        slug=str(x),
    #                                        author_data={'username_a': f'{x}'})
    #         total_recipes.append(x.title)

    #     show_total_recipes_in_page = len(
    #         response.context['recipes'].object_list)
    #     print(len(total_recipes))
    #     self.assertEqual(show_total_recipes_in_page, 10)
