# POUR CALCULER LES INGREDIENTS REQUIS


# Quelles sont les recettes saisies et leurs ingrédients respectifs ?


def get_required_meals_and_ingredients(l_entered_meals, l_meals_and_ingredients):
    """Renvoie une liste de dictionnaires associant un plat saisi à ses ingrédients."""
    l_required_meals_and_ingredients = []
    for meal_and_ingredients in l_meals_and_ingredients:
        if meal_and_ingredients['meal name'] in l_entered_meals:
            l_required_meals_and_ingredients.append(meal_and_ingredients)
    return l_required_meals_and_ingredients




# Quels ingrédients sont requis et en quelle quantité, toute recette confondue ?


def get_required_ingredients(l_entered_meals, l_meals_and_ingredients):
    """Renvoie un dictionnaire associant chaque ingrédient à sa quantité requise
    (les ingrédients dont la quantité requise est nulle sont ignorés)."""
    l_required_meals_and_ingredients = get_required_meals_and_ingredients(l_entered_meals, l_meals_and_ingredients)
    dict_required_ingredients = dict()
    for meal_and_ingredients in l_required_meals_and_ingredients:
        for ingredient in meal_and_ingredients['ingredients']:
            if not ingredient in dict_required_ingredients:
                dict_required_ingredients[ingredient] = 0
            dict_required_ingredients[ingredient] += meal_and_ingredients['ingredients'][ingredient]
    return dict_required_ingredients




# Quelles sont les unités des quantités des ingrédients requis ?


def get_correct_unit(ingredient, dict_units):
    for unit in dict_units:
        if ingredient in dict_units[unit]:
            correct_unit = unit
    return correct_unit