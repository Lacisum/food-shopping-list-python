# LECTURE DU DOCUMENT TEXTE CONTENANT LES PLATS ET LEURS INGREDIENTS

import re

# Pour analyser une ligne et vérifier si elle contient le nom d'un plat (ligne-plat)
#  ou bien un ingrédient et sa quantité (ligne-ingrédient)

def is_meal_line(line):
    """ Vérifie si une ligne contient le nom d'un plat."""
    return bool(re.match("\s*(.+[^\s])\s*:\s*", line))

def is_ingredient_line(line):
    """ Vérifie si une ligne contient le nom d'un ingredient."""
    return bool(re.match("\s*-\s*(.+[^\s])\s+\(([0-9]+|[0-9]+.[0-9]+)\s+(.*)\)", line))


# Pour extraire les données d'une ligne

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
    match = re.search("\s*-\s*(.+[^\s])\s+\(([0-9]+|[0-9]+.[0-9]+)\s+(.*)\)", ingr_line)
    ingr_infos["name"] = match.group(1)
    ingr_infos["quantity"] = match.group(2)
    ingr_infos["unit"] = match.group(3) if match != None else None
    return ingr_infos

def get_meal(meal_line):
    """ Renvoie le nom du plat d'une ligne-plat.
    Exemples:
    >>> get_meal(' tofu basquaise : ')
    'tofu basquaise'
    """
    match = re.search("\s*(.+[^\s])\s*:\s*", meal_line)
    return match.group(1)


# Pour lire le fichier texte contenant les plats et les ingrédients et intégrer son contenu dans :
# - l_meals_and_ingr (liste associant chaque plat à des ingrédients) et
# - dict_units (dictionnaire associant chaque nom d'unité à une liste d'ingrédients)

def integrate_file_data(file_name, l_meals_and_ingredients, dict_units):
    """
    Intègre les données d'un fichier de plats et d'ingrédients dans les variables l_meals_and_ingr et dict_units.
    En particulier :
    - met les noms de plats, les noms d'ingrédients et les quantités d'ingrédients dans l_meals_and_ingr
    - met les noms des unités correspondant aux ingrédients dans dict_units
    """

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

                ingr_infos = get_ingr_infos(line)
                ingredient = ingr_infos['name']   # le nom de l'ingrédient en cours de traitement
                quantity = ingr_infos['quantity']       # la quantité de l'ingrédient en cours de traitement
                unit = ingr_infos['unit']               # l'unité de l'ingrédient en cours de traitement

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




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)