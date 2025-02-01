from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
# from .utils.recipes.factory_recipe import make_recipe
from .models import Recipe

# functions based views


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('created_at')

    context = {
        'recipes': recipes,
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

    context = {
        'recipes': recipes,
        'name_category': f'{recipes[0].category.name}'
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
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
    })
