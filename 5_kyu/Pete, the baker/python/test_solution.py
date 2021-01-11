import pytest

from solution import cakes


data_basic_recipes = [
    (
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
        2,
    ),
    (
        {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000},
        11,
    ),
]


@pytest.mark.parametrize("recipe, available, num_cakes", data_basic_recipes)
def test_basic_recipes(recipe, available, num_cakes):
    assert cakes(recipe, available) == num_cakes


data_missing_ingredient = [
    (
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
        0,
    ),
]


@pytest.mark.parametrize("recipe, available, num_cakes", data_missing_ingredient)
def test_missing_ingredient(recipe, available, num_cakes):
    assert cakes(recipe, available) == num_cakes


data_not_enough_ingredients = [
    (
        {"eggs": 4, "flour": 400},
        {},
        0,
    ),
]


@pytest.mark.parametrize("recipe, available, num_cakes", data_not_enough_ingredients)
def test_not_enough_ingredients(recipe, available, num_cakes):
    assert cakes(recipe, available) == num_cakes


data_exactly_enough_ingredients_for_one_cake = [
    (
        {"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},
        {"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1},
        1,
    ),
]


@pytest.mark.parametrize(
    "recipe, available, num_cakes", data_exactly_enough_ingredients_for_one_cake
)
def test_exactly_enough_ingredients_for_one_cake(recipe, available, num_cakes):
    assert cakes(recipe, available) == num_cakes
