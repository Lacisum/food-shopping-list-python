# Ce programme donne les ingrédients requis pour faire les recettes désirées.

from file_parsing import *
from input_parsing import *
from display import *
from ingredients_computation import *



# SAISIE DES RECETTES DESIREES

def meals_input():
    """Invite l'utilisateurice à saisir un ou des plats."""
    print('\nSaisis le ou les plat(s) que tu veux faire. Par exemple :\n')
    print('     "tofu basquaise, patates sautées"\n')
    res = input()
    return res




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