# POUR L'AFFICHAGE


def presentation(L_MEALS):
    """Imprime la présentation du programme, y compris la liste des plats."""
    print('Ce programme te donne la liste des ingrédients requis pour faire les plats que tu choisis.\n')
    print('Voici la liste des plats disponibles :\n')
    for meal in L_MEALS:
        print(f'- {meal}')


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