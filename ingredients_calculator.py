# Ce programme donne les ingrédients requis pour faire les recettes désirées.




# LECTURE DU DOCUMENT TEXTE CONTENANT LES PLATS ET LEURS INGREDIENTS


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


# Pour analyser une ligne et vérifier si elle contient le nom d'un plat (ligne-plat)
#  ou bien un ingrédient et sa quantité (ligne-ingrédient)

def is_meal_line(line):
    """ Vérifie si une ligne contient le nom d'un plat."""
    return line[0].isalpha()

def is_ingredient_line(line):
    """ Vérifie si une ligne contient le nom d'un ingredient."""
    return line[0:2] == "- "


# Pour extraire les données d'une ligne

def get_meal(meal_line):
    """ Extrait le nom du plat d'une ligne-plat.
    Exemples:
    >>> get_meal('tofu basquaise :')
    'tofu basquaise'
    """
    meal = ""
    i = 0
    while i < len(meal_line)-1 and meal_line[i:i+2] != " :":
        meal += meal_line[i]
        i += 1
    return meal

def get_ingredient(ingr_line):
    """ Extrait le nom de l'ingrédient d'une ligne-ingrédient.
    Exemples:
    >>> get_ingredient('- patates (1 kg)')
    'patates'
    """
    ingr = ''
    i = 2
    while i < len(ingr_line)-1 and ingr_line[i:i+2] != ' (':
        ingr += ingr_line[i]
        i += 1
    return ingr

def get_quantity(ingr_line):
    """ Extrait la quantité de l'ingrédient d'une ligne-ingrédient.
    Exemples:
    >>> get_quantity('- patates (1 kg)')
    '1'
    """
    quantity = ''
    i = 2
    while i < len(ingr_line) and ingr_line[i] != '(':
        i += 1
    i += 1
    while i < len(ingr_line) and ingr_line[i] != ' ' and ingr_line[i] != ')':
        quantity += ingr_line[i]
        i += 1
    return quantity

def get_unit(ingr_line):
    """ Extrait l'unité de la quantité de l'ingrédient d'une ligne-ingrédient.
    Exemples:
    >>> get_unit('- patates (1 c à s)')
    'c à s'
    >>> get_unit('- ognons (1)')
    ''
    """
    unit = ''
    i = len(ingr_line)-1
    while i >= 0 and ingr_line[i] != ')':
        i -= 1
    i -= 1
    while i >= 1 and not ingr_line[i].isdigit() and not (ingr_line[i] == ' ' and ingr_line[i-1].isdigit()) and ingr_line[i] != '(':
        unit = ingr_line[i] + unit
        i -= 1
    return unit


# Pour lire le fichier texte contenant les plats et les ingrédients et intégrer son contenu dans :
# - l_meals_and_ingr (liste associant chaque plat à des ingrédients) et
# - dict_units (dictionnaire associant chaque nom d'unité à une liste d'ingrédients)

def integrate_file_data(file_name):
    """
    Intègre les données d'un fichier de plats et d'ingrédients dans les variables l_meals_and_ingr et dict_units.
    En particulier :
    - met les noms de plats, les noms d'ingrédients et les quantités d'ingrédients dans l_meals_and_ingr
    - met les noms des unités correspondant aux ingrédients dans dict_units
    """
    global l_meals_and_ingredients
    global dict_units

    with open(file_name, 'rt', encoding='utf8') as input:

        have_treated_at_least_one_meal_line = False # a-t-on déjà traité au moins un plat ? Pour l'instant, non -> False
        dict_ingredients = dict() # dictionnaire associant chaque ingrédient d'un plat donné à une quantité (sans unité)
        line = input.readline() # la ligne en cours de traitement

        # Tant qu'on n'est pas arrivé à la fin du fichier :
        while line != "":

            # Si la ligne est une ligne-plat :
            if is_meal_line(line):

                # Si ce n'est pas la première ligne-plat qu'on traite :
                if have_treated_at_least_one_meal_line:
                    # Enregistrer le plat précédent et ses ingrédients dans l_meals_and_ingredients
                    dict_meal_and_ingredients = {'meal': meal, 'ingredients': dict_ingredients}
                    l_meals_and_ingredients.append(dict_meal_and_ingredients)
                    # Vider le dictionnaire ingredients
                    dict_ingredients = dict()

                # Mettre le nom du plat dans meal
                meal = get_meal(line)
                # Signaler qu'on a déjà traité au moins une ligne-plat
                have_treated_at_least_one_meal_line = True

            # Sinon, si la ligne est une ligne-ingrédient :
            elif is_ingredient_line(line):

                ingredient = get_ingredient(line) # ingredient : le nom de l'ingrédient en cours de traitement
                quantity = get_quantity(line)       # quantity : la quantité de l'ingrédient en cours de traitement
                unit = get_unit(line)                   # unit : l'unité de l'ingrédient en cours de traitement

                # Ajouter l'ingrédient et sa quantité dans le dictionnaire ingredients.
                dict_ingredients[ingredient] = quantity

                # Traitement des unités d'ingrédients :
                if not unit in dict_units:
                    dict_units[unit] = [ingredient]
                else:
                    if not ingredient in dict_units[unit]:
                        dict_units[unit].append(ingredient)
            
            # Si la ligne n'est ni une ligne-plat ni une ligne-ingrédient, ne rien faire.
                
            # Lire la ligne suivante
            line = input.readline()
        
        # Quand on a fini de lire le fichier, on enregistre le tout dernier plat (et ses ingrédients associés).
        dict_meal_and_ingredients = {'meal': meal, 'ingredients': dict_ingredients}
        l_meals_and_ingredients.append(dict_meal_and_ingredients)




integrate_file_data('meals_and_ingredients.txt')

# LISTE DES RECETTES

L_MEALS = [l_meals_and_ingredients[i]['meal'] for i in range(len(l_meals_and_ingredients))]




# PRESENTATION

def presentation():
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




# QUELLES RECETTES ONT ETE SAISIES ?

def meal_is_entered(meal, input):
    """Renvoie True si un plat donné est écrit dans une chaine donnée, False sinon.
    Exemples :
    >>> meal_is_entered('patates sautées', 'je veux des patates sautées  ')
    True
    """
    res = False
    i = 0
    while i + len(meal) <= len(input) and res == False:
        if input[i:i+len(meal)] == meal:
            res = True
        else:
            i += 1
    return res

def get_entered_meals(input):
    """Renvoie la liste des plats saisis par l'utilisateurice.
    Exemples :
    >>> get_entered_meals('salade de patates')
    ['salade de patates']
    >>> get_entered_meals('salade de patates et patates sautées u1(ù$')
    ['salade de patates', 'patates sautées']
    >>> get_entered_meals('patates sautees')
    []
    >>> get_entered_meals('canapé')
    []
    """
    global L_MEALS
    l_entered_meals = []
    i = 0
    while i < len(L_MEALS):
        if meal_is_entered(L_MEALS[i], input):
            l_entered_meals.append(L_MEALS[i])
        i += 1
    return l_entered_meals




# AFFICHAGE DES RECETTES SAISIES

def display_entered_meals(l_entered_meals):
    """Affiche les plats saisies par l'utilisateurice."""
    print('\nTu as saisi les plats suivantes :\n')
    for entered_meal in l_entered_meals:
        print(f'- {entered_meal}')
    return None




def get_required_meals_and_ingredients(l_entered_meals):
    """Renvoie une liste de dictionnaires associant un plat saisi à ses ingrédients."""
    global l_meals_and_ingredients
    l_required_meals_and_ingredients = []
    for meal_and_ingredients in l_meals_and_ingredients:
        if meal_and_ingredients['meal'] in l_entered_meals:
            l_required_meals_and_ingredients.append(meal_and_ingredients)
    return l_required_meals_and_ingredients




# QUELS INGREDIENTS SONT REQUIS ET EN QUELLE QUANTITE ?

def get_required_ingredients(l_entered_meals):
    """Renvoie un dictionnaire associant chaque ingrédient à sa quantité requise
    (les ingrédients dont la quantité requise est nulle sont ignorés)."""
    l_required_meals_and_ingredients = get_required_meals_and_ingredients(l_entered_meals)
    dict_required_ingredients = dict()
    for meal_and_ingredients in l_required_meals_and_ingredients:
        for ingredient in meal_and_ingredients['ingredients']:
            dict_required_ingredients[ingredient] += meal_and_ingredients['ingredients'][ingredient]
    return dict_required_ingredients




# AFFICHAGE DES INGREDIENTS REQUIS, QUANTITES COMPRISES

def get_correct_unit(ingredient):
    for unit in dict_units:
        if ingredient in dict_units[unit]:
            correct_unit = unit
    return correct_unit

def display_required_ingredients(dict_required_ingredients):
    """Affiche les ingrédients requis, quantités comprises."""
    print('\nVoici les ingrédients requis :\n')
    for ingredient in dict_required_ingredients:
        quantity = dict_required_ingredients[ingredient]
        unit = get_correct_unit(ingredient)
        print(f'- {ingredient}  {round(quantity, 3)}{unit}')
    return None




# FONCTION PRINCIPALE

def main_ingredients():
    presentation()
    input = meals_input()
    l_entered_meals = get_entered_meals(input)
    display_entered_meals(l_entered_meals)
    dict_required_ingredients = get_required_ingredients(l_entered_meals)
    display_required_ingredients(dict_required_ingredients)




if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main_ingredients()
    # integrate_file_data('meals_and_ingredients.txt')
    # print(l_meals_and_ingredients)
    # print()
    # print(dict_units)
    # print()
    # print(L_MEALS)