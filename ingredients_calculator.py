# Ce programme donne les ingrédients requis pour faire les recettes désirées.

from file_parsing import *

from file_parsing import *
from input_parsing import *



# PRESENTATION

def presentation(L_MEALS):
    """Imprime la présentation du programme, y compris la liste des plats."""
    print('Ce programme te donne la liste des ingrédients requis pour faire les plats que tu choisis.\n')
    print('Voici la liste des plats disponibles :\n')
    for meal in L_MEALS:
        print(f'- {meal}')




# SAISIE DES RECETTES DESIREES

def meals_input():
    """Invite l'utilisateurice à saisir un ou des plats."""
    print('\nSaisis le ou les plat(s) que tu veux faire. Par exemple :\n')
    print('     "tofu basquaise, patates sautées"\n')
    res = input()
    return res




# AFFICHAGE DES RECETTES SAISIES

def display_entered_meals(l_entered_meals):
    """Affiche les plats saisies par l'utilisateurice."""
    print('\nTu as saisi les plats suivantes :\n')
    for entered_meal in l_entered_meals:
        print(f'- {entered_meal}')
    return None




def get_required_meals_and_ingredients(l_entered_meals, l_meals_and_ingredients):
    """Renvoie une liste de dictionnaires associant un plat saisi à ses ingrédients."""
    l_required_meals_and_ingredients = []
    for meal_and_ingredients in l_meals_and_ingredients:
        if meal_and_ingredients['meal'] in l_entered_meals:
            l_required_meals_and_ingredients.append(meal_and_ingredients)
    return l_required_meals_and_ingredients




# QUELS INGREDIENTS SONT REQUIS ET EN QUELLE QUANTITE ?

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




# AFFICHAGE DES INGREDIENTS REQUIS, QUANTITES COMPRISES

def get_correct_unit(ingredient, dict_units):
    for unit in dict_units:
        if ingredient in dict_units[unit]:
            correct_unit = unit
    return correct_unit

def display_required_ingredients(dict_required_ingredients, dict_units):
    """Affiche les ingrédients requis, quantités comprises."""
    print('\nVoici les ingrédients requis :\n')
    for ingredient in dict_required_ingredients:
        quantity = dict_required_ingredients[ingredient]
        unit = get_correct_unit(ingredient, dict_units)
        print(f'- {ingredient}  {round(quantity, 3)}{unit}')
    return None




# FONCTION PRINCIPALE

def main_ingredients():

    # Liste de dictionnaires associant un plat à ses ingrédients

    # Cette liste sera une liste de dictionnaire à deux clés.
    # Les deux clés sont le nom d'un plat (string) et les ingrédients (dict).
    # La deuxième clé, un dictionnaire, associera chaque ingrédient du plat à la quantité de l'ingrédient (à un nombre).

    # Exemple :
    #            [{'meal': 'riz cantonnais', 
    #              'ingredients': {'riz': '0.14',
    #                              'petit pois': '0.05',
    #                              'saucisse de soja': '2'}
    #             },
    #             {'meal': 'tofu basquaise',
    #              'ingredients': {'riz': '0.3',
    #                              'tofu': '0.2'}
    #             }
    #            ]
    l_meals_and_ingredients = list()

    # Dictionnaire associant chaque nom d'unité à une liste d'ingrédients

    # Exemple :
    #           {'kg': ['patates', 'tofu'], 
    #            'c à s': ['huile', 'vinaigre']}
    dict_units = dict()

    integrate_file_data('meals_and_ingredients.txt', l_meals_and_ingredients, dict_units)
    L_MEALS = [l_meals_and_ingredients[i]['meal'] for i in range(len(l_meals_and_ingredients))] # liste des recettes

    presentation(L_MEALS)
    input = meals_input()
    l_entered_meals = get_entered_meals(input, L_MEALS)
    display_entered_meals(l_entered_meals)
    dict_required_ingredients = get_required_ingredients(l_entered_meals, l_meals_and_ingredients)
    display_required_ingredients(dict_required_ingredients, dict_units)




if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main_ingredients()