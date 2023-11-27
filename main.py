# CE PROGRAMME DONNE LA LISTE DES INGREDIENTS REQUIS (ET LEURS QUANTITES)
# POUR FAIRE LES RECETTES DESIRES

import sys

from secondary_functions import *


def main(argv):


    if len(argv) != 2:
        print('Usage: python3 main.py <file_name>')
        exit(1)


    # Liste de dictionnaires associant un plat à ses ingrédients
    l_meals_and_ingredients = list()
    # Cette liste sera une liste de dictionnaire à deux clés.
    # Les deux clés sont le nom d'un plat (string) et les ingrédients (dict).
    # La deuxième clé, un dictionnaire, associera chaque ingrédient du plat à la quantité de l'ingrédient (un nombre).
    # Les unités des quantités des ingrédients seront quant à elles stockées dans le dictionnaire dict_units.
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


    # Dictionnaire associant chaque nom d'unité à une liste d'ingrédients
    dict_units = dict()
    # Exemple :
    #           {'kg': ['patates', 'tofu'], 
    #            'c à s': ['huile', 'vinaigre']}


    integrate_file_data(argv[1], l_meals_and_ingredients, dict_units)
    presentation(l_meals_and_ingredients)
    input = meals_input()
    l_entered_meals = get_entered_meals(input, l_meals_and_ingredients)
    display_entered_meals(l_entered_meals)
    dict_required_ingredients = get_required_ingredients(l_entered_meals, l_meals_and_ingredients)
    display_required_ingredients(dict_required_ingredients, dict_units)




if __name__ == '__main__':
    main(sys.argv)