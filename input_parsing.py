# QUELLES RECETTES ONT ETE SAISIES ?


import re

def meal_is_entered(meal_name, input):
    """Renvoie True si un plat donné est écrit dans une chaine donnée, False sinon.
    Exemples :
    >>> meal_is_entered('patates sautées', 'je veux des patates sautées  ')
    True
    """
    return re.search(meal_name, input)

def get_entered_meals(input, L_MEALS):
    """Renvoie la liste des plats saisis par l'utilisateurice.
    Exemples :
    >>> get_entered_meals('salade de patates', ['salade de patates', 'patates sautées'])
    ['salade de patates']
    >>> get_entered_meals('salade de patates et patates sautées u1(ù$', ['salade de patates', 'patates sautées'])
    ['salade de patates', 'patates sautées']
    >>> get_entered_meals('patates sautees', ['salade de patates', 'patates sautées'])
    []
    >>> get_entered_meals('canapé', ['salade de patates', 'patates sautées'])
    []
    """
    l_entered_meals = []
    for meal_name in L_MEALS:
        if meal_is_entered(meal_name, input):
            l_entered_meals.append(meal_name)
    return l_entered_meals