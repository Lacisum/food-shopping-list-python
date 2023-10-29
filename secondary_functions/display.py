# POUR L'AFFICHAGE


from .ingredients_computation import get_correct_unit


def presentation(l_meals_and_ingredients):
    """Imprime la présentation du programme, y compris la liste des plats."""
    print('Ce programme te donne la liste des ingrédients requis pour faire les plats que tu choisis.\n')
    print('Voici la liste des plats disponibles :\n')
    for meal in l_meals_and_ingredients:
        print(f"- {meal['meal name']}")


def meals_input():
    """Invite l'utilisateurice à saisir un ou des plats."""
    print('\nSaisis le ou les plat(s) que tu veux faire. Par exemple :\n')
    print('     "tofu basquaise, patates sautées"\n')
    res = input()
    return res


def display_entered_meals(l_entered_meals):
    """Affiche les plats saisies par l'utilisateurice."""
    print('\nTu as saisi les plats suivantes :\n')
    for entered_meal in l_entered_meals:
        print(f'- {entered_meal}')
    return None


def display_required_ingredients(dict_required_ingredients, dict_units):
    """Affiche les ingrédients requis, quantités comprises."""
    print('\nVoici les ingrédients requis :\n')
    for ingredient in dict_required_ingredients:
        quantity = dict_required_ingredients[ingredient]
        unit = get_correct_unit(ingredient, dict_units)
        print(f'- {ingredient}  {round(quantity, 3)}{unit}')
    return None