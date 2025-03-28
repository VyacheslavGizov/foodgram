from datetime import datetime


REPORT_TITLE = 'СПИСОК ПОКУПОК'
CREATED_DATE = 'составлен {:%d.%m.%Y}'
INGREDIENTS_TITLE = '\nПродукты:'
INGREDIENT_FORMAT = '{} ({}): {}'
LINE_FORMAT = '  {}. {}'
RECIPES_TITLE = '\nДля приготовления:'
RECIPE_FORMAT = '  - {}'


def render_shopping_cart(recipes, ingredients):
    return '\n'.join([
        REPORT_TITLE,
        CREATED_DATE.format(datetime.now()),
        INGREDIENTS_TITLE,
        *[LINE_FORMAT.format(
            number,
            INGREDIENT_FORMAT.format(*ingredient).capitalize()
        ) for number, ingredient in enumerate(ingredients, 1)],
        RECIPES_TITLE,
        *[RECIPE_FORMAT.format(recipe.name) for recipe in recipes]
    ])
