from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
from django.db.models import Q

from .utils.pagination import make_pagination
import os

# from .utils.recipes.factory_recipe import make_recipe
# functions based views

PER_PAGE = os.environ.get('PER_PAGE')


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('created_at')

    page_obj, patinagion_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        'recipes': page_obj,
        'patinagion_range': patinagion_range
    }
    return render(request, 'recipes/pages/home.html', context)


def category(request, id_category):
    # recipes = Recipe.objects.filter(category__id=id_category,
    #                                 is_published=True).order_by('created_at')
    # if not recipes:
    #     raise Http404('Not found :,(')

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=id_category,
                              is_published=True).order_by('created_at')
    )

    page_obj, patinagion_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        'recipes': page_obj,
        'name_category': f'{recipes[0].category.name}',
        'patinagion_range': patinagion_range
    }
    return render(request, 'recipes/pages/category.html', context)


def recipes(request, id):

    # recipe = Recipe.objects.filter(
    #     id=id, is_published=True).order_by('created_at').first()

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    context = {
        'recipe': recipe,
        'is_datail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context)


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        ),
        is_published=True,
    ).order_by('-id')

    page_obj, patinagion_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'patinagion_range': patinagion_range,
        "additional_url_query": f'&search={search_term}'
    })
