# POUR L'AFFICHAGE

import re

from .ingredients_computation import get_correct_unit


def presentation(l_meals_and_ingredients):
    """Imprime la présentation du programme, y compris la liste des plats."""
    print()
    print('Ce programme te donne la liste des ingrédients requis pour réaliser les recettes que tu choisis.\n')
    print('Voici la liste des recettes disponibles :')
    for meal in l_meals_and_ingredients:
        print(f"- {meal['meal name']}")
    print()


def meals_input():
    """Invite l'utilisateurice à saisir une ou des recettes."""
    print('Saisis la/les recette(s) que tu veux réaliser.')
    res = input()
    print()
    return res


def display_entered_meals(l_entered_meals):
    """Affiche les recettes saisies par l'utilisateurice."""
    print('Tu as saisi les recettes suivantes :')
    for entered_meal in l_entered_meals:
        print(f'- {entered_meal}')
    print()


def display_required_ingredients(dict_required_ingredients, dict_units):
    """Affiche les ingrédients requis, quantités comprises."""
    print('Voici tous les ingrédients requis :')
    max_ingr_name_length = max(map(lambda ingr_name : len(ingr_name), dict_required_ingredients))
    for ingr_name in dict_required_ingredients:
        if dict_required_ingredients[ingr_name].is_integer():
            quantity = int(dict_required_ingredients[ingr_name])
        else:
            quantity = round(dict_required_ingredients[ingr_name], 3)
        unit = get_correct_unit(ingr_name, dict_units)
        print('- {}{} {}'.format(ingr_name.ljust(max_ingr_name_length+4, '.'), quantity, unit))