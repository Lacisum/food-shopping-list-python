# LECTURE DU DOCUMENT TEXTE CONTENANT LES PLATS ET LEURS INGREDIENTS


import re


# Pour vérifier si une ligne contient le nom d'un plat (ligne-plat) ou bien un ingrédient et sa quantité (ligne-ingrédient)


def is_meal_line(line):
    """ Vérifie si une ligne contient le nom d'un plat."""
    return bool(re.match("\s*(.+[^\s])\s*:\s*", line))


def is_ingredient_line(line):
    """ Vérifie si une ligne contient le nom d'un ingredient."""
    return bool(re.match("\s*-\s*(.+[^\s])\s+\(([0-9]+|[0-9]+.[0-9]+)\s*(.*)\)", line))




# Pour lire les informations d'une ligne


def get_ingr_infos(ingr_line):
    """
    Renvoie le match correspondant au pattern d'une ligne-ingrédient.
    Exemples:
    >>> ingr_infos = get_ingr_infos('- patates (1 kg)')
    >>> ingr_infos['name']
    'patates'
    >>> ingr_infos['quantity']
    '1'
    >>> ingr_infos['unit']
    'kg'
    """
    ingr_infos = dict()
    match = re.search("\s*-\s*(.+[^\s])\s+\(([0-9]+.[0-9]+|[0-9]+)\s*(.*)\)", ingr_line)
    ingr_infos["name"] = match.group(1)
    ingr_infos["quantity"] = match.group(2)
    ingr_infos["unit"] = match.group(3) if match != None else None
    return ingr_infos


def get_meal_name(meal_line):
    """ Renvoie le nom du plat d'une ligne-plat.
    Exemples:
    >>> get_meal_name(' tofu basquaise : ')
    'tofu basquaise'
    """
    match = re.search("\s*(.+[^\s])\s*:\s*", meal_line)
    return match.group(1)




# Pour enregistrer les informations d'une ligne


def treat_line(line, l_meals_and_ingredients, dict_units, meal_name, dict_ingredients):
    if is_meal_line(line):
        meal_name = treat_meal_line(line, l_meals_and_ingredients, dict_ingredients, meal_name)
    elif is_ingredient_line(line):
        treat_ingredient_line(line, dict_units, dict_ingredients)
    # On ignore les lignes qui ne sont ni des lignes-plats ni des lignes-ingrédients
    return meal_name


def treat_meal_line(line, l_meals_and_ingredients, dict_ingredients, meal_name):
    if meal_name != None: # si l'on a déjà traité une ligne-plat
        register_meal(l_meals_and_ingredients, dict_ingredients.copy(), meal_name) # enregistrer le plat précédemment lu
        dict_ingredients.clear()
    return get_meal_name(line)


def register_meal(l_meals_and_ingredients, dict_ingredients, meal_name):
    l_meals_and_ingredients.append({'meal name': meal_name, 'ingredients': dict_ingredients})


def treat_ingredient_line(line, dict_units, dict_ingredients):
    ingr_infos = get_ingr_infos(line)
    ingr_name = ingr_infos['name']                  # le nom de l'ingrédient en cours de traitement
    ingr_quantity = float(ingr_infos['quantity'])   # la quantité de l'ingrédient en cours de traitement
    ingr_unit = ingr_infos['unit']                  # l'unité de l'ingrédient en cours de traitement
    dict_ingredients[ingr_name] = ingr_quantity
    treat_ingr_unit(dict_units, ingr_name, ingr_unit)


def treat_ingr_unit(dict_units, ingr_name, ingr_unit):
    if not ingr_unit in dict_units:
        dict_units[ingr_unit] = [ingr_name]
    else:
        if not ingr_name in dict_units[ingr_unit]:
            dict_units[ingr_unit].append(ingr_name)




# Pour lire le fichier texte contenant les plats et les ingrédients et intégrer son contenu dans l_meals_and_ingr et dict_units


def integrate_file_data(file_name, l_meals_and_ingredients, dict_units):
    """
    Intègre les données d'un fichier de plats et d'ingrédients dans les variables l_meals_and_ingr et dict_units.
    En particulier :
    - met les noms de plats, les noms d'ingrédients et les quantités d'ingrédients dans l_meals_and_ingr
    - met les noms des unités correspondant aux ingrédients dans dict_units
    """
    with open(file_name, 'rt', encoding='utf8') as input:
        meal_name = None
        dict_ingredients = dict() # dictionnaire associant chaque ingrédient d'un plat donné à une quantité (sans unité)
        line = input.readline() # la ligne en cours de traitement
        while line != "":  # tant qu'on n'est pas arrivé à la fin du fichier
            meal_name = treat_line(line, l_meals_and_ingredients, dict_units, meal_name, dict_ingredients)    
            line = input.readline() # lit la ligne suivante
    register_meal(l_meals_and_ingredients, dict_ingredients, meal_name) # Quand on a fini de lire le fichier, on enregistre les informations du tout dernier plat




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)