# QUELLES RECETTES ONT ETE SAISIES ?


import re

def meal_is_entered(meal_name, input):
    """Renvoie True si un plat donné est écrit dans une chaine donnée, False sinon.
    Exemples :
    >>> meal_is_entered('patates sautées', 'je veux des patates sautées  ')
    True
    """
    return re.search(meal_name, input)

def get_entered_meals(input, l_meals_and_ingredients):
    """Renvoie la liste des plats saisis par l'utilisateurice.
    Exemples :
    >>> get_entered_meals('salade de patates', [{'meal name': 'salade de patates', 'ingredients': dict()}, \
                                                {'meal name': 'patates sautées', 'ingredients': dict()}])
    ['salade de patates']
    >>> get_entered_meals('salade de patates et patates sautées u1(ù$', [{'meal name': 'salade de patates', 'ingredients': dict()}, \
                                                                         {'meal name': 'patates sautées', 'ingredients': dict()}])
    ['salade de patates', 'patates sautées']
    >>> get_entered_meals('patates sautees', [{'meal name': 'salade de patates', 'ingredients': dict()}, \
                                              {'meal name': 'patates sautées', 'ingredients': dict()}])
    []
    >>> get_entered_meals('canapé', [{'meal name': 'salade de patates', 'ingredients': dict()}, \
                                     {'meal name': 'patates sautées', 'ingredients': dict()}])
    []
    """
    l_entered_meals = []
    for meal in l_meals_and_ingredients:
        if meal_is_entered(meal['meal name'], input):
            l_entered_meals.append(meal['meal name'])
    return l_entered_meals