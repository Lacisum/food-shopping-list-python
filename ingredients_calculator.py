# Ce programme donne les ingrédients requis pour faire les recettes désirées.


# LISTE DES RECETTES

L_REC = ['salade de patates',
         'patates sautées',
         'riz cantonnais',
         'tofu basquaise']


# PRESENTATION

def presentation():
    """Imprime la présentation du programme, y compris la liste des recettes."""
    print('Ce programme te donne la liste des ingrédients requis pour faire les recettes que tu choisis.\n')
    print('Voici la liste des recettes disponibles :\n')
    for rec in L_REC:
        print(f'- {rec}')


# SAISIE DES RECETTES DESIREES

def saisie_de_recettes():
    """Invite l'utilisateurice à saisir une ou des recettes souhaitées."""
    print('\nSaisis la ou les recette(s) que tu veux faire. Par exemple :\n')
    print('     "tofu basquaise, patates sautées"\n')
    s = input()
    return s


# QUELLES RECETTES ONT ETE SAISIES ?

def recette_est_saisie(rec, s):
    """Renvoie True si une recette donnée est écrite dans une chaine de caractères, False sinon.
    Exemples :
    >>> recette_est_saisie('patates sautées', 'je veux des patates sautées  ')
    True
    """
    res = False
    i = 0
    while i + len(rec) <= len(s) and res == False:
        if s[i:i+len(rec)] == rec:
            res = True
        else:
            i += 1
    return res

def recettes_saisies(s):
    """Renvoie la liste des recettes saisies par l'utilisateurice.
    Exemples :
    >>> recettes_saisies('salade de patates')
    ['salade de patates']
    >>> recettes_saisies('salade de patates et patates sautées u1(ù$')
    ['salade de patates', 'patates sautées']
    >>> recettes_saisies('patates sautees')
    []
    >>> recettes_saisies('canapé')
    []
    """
    global L_REC
    l_rec_saisies = []
    i = 0
    while i < len(L_REC):
        if recette_est_saisie(L_REC[i], s):
            l_rec_saisies.append(L_REC[i])
        i += 1
    return l_rec_saisies


# AFFICHAGE DES RECETTES SAISIES

def affiche_recettes_saisies(l_rec_saisies):
    """Affiche les recettes saisies par l'utilisateurice."""
    print('\nTu as saisi les recettes suivantes :\n')
    for rec_saisie in l_rec_saisies:
        print(f'- {rec_saisie}')
    return None


# LISTE DES INGREDIENTS

## Liste des ingrédients par unités de mesure

l_ingr_kg = ["patates",
             "salade",
             "tofu",
             "riz",
             "petits pois",
             "tomates"]

l_ingr_unit = ["ognons",
               "échalottes",
               "gousses d'ail",
               "saucisse de soja",
               "poivrons"]

l_ingr_cs = ["huile",
             "vinaigre"]

l_ingr_pincee = ["sel",
                 "poivre",
                 "paprika",
                 "piment"]

l_ingr_branche = ["thym"]

## Liste de tous les ingrédients

l_tous_ingr = l_ingr_kg.copy()
l_tous_ingr += l_ingr_unit
l_tous_ingr += l_ingr_cs
l_tous_ingr += l_ingr_pincee
l_tous_ingr += l_ingr_branche

## Dictionnaire contenant tous les ingrédients et leur quantité (initialisée à 0)

d_ingr = dict([(ingr, 0) for ingr in l_tous_ingr])


# FONCTIONS DE RECETTES

def salade_de_patates():
    global d_ingr
    d_ingr["patates"] += 1.5
    d_ingr["salade"] += 0.1
    d_ingr["échalottes"] += 1
    d_ingr["huile"] += 2
    d_ingr["vinaigre"] += 1
    d_ingr["sel"] += 1
    d_ingr["poivre"] += 4
    return None

def patates_sautees():
    global d_ingr
    d_ingr["patates"] += 1.5
    d_ingr["salade"] += 0.1
    d_ingr["tofu"] += 0.2
    d_ingr["échalottes"] += 1
    d_ingr["huile"] += 8
    d_ingr["vinaigre"] += 1
    d_ingr["sel"] += 2
    d_ingr["poivre"] += 4
    return None

def riz_cantonnais():
    global d_ingr
    d_ingr["riz"] += 0.14
    d_ingr["saucisse de soja"] += 2
    d_ingr["petits pois"] += 0.05
    d_ingr["huile"] += 2
    d_ingr["sel"] += 1
    return None

def tofu_basquaise():
    global d_ingr
    d_ingr["riz"] += 0.1
    d_ingr["tofu"] += 0.1
    d_ingr["ognons"] += 1
    d_ingr["gousses d'ail"] += 1
    d_ingr["poivrons"] += 1
    d_ingr["tomates"] += 0.15
    d_ingr["huile"] += 4
    d_ingr["sel"] += 1
    d_ingr["poivre"] += 1
    d_ingr["paprika"] += 3
    d_ingr["piment"] += 3
    return None


# APPEL DES FONCTIONS DE RECETTES

def fonctions_de_recette_a_appeler(l_rec_saisies):
    """Renvoie les fonctions de recettes à appeler à partir de la liste des recettes saisies."""
    l_fonctions_a_appeler = []
    for rec_saisie in l_rec_saisies:
        if rec_saisie == 'salade de patates':
            l_fonctions_a_appeler.append(salade_de_patates)
        elif rec_saisie == 'patates sautées':
            l_fonctions_a_appeler.append(patates_sautees)
        elif rec_saisie == 'riz cantonnais':
            l_fonctions_a_appeler.append(riz_cantonnais)
        elif rec_saisie == 'tofu basquaise':
            l_fonctions_a_appeler.append(tofu_basquaise)
    return l_fonctions_a_appeler
    
def appel_fonctions_de_recette(l_fonctions_a_appeler):
    """Appelle les fonctions de recettes qu'il faut appeler."""
    for f in l_fonctions_a_appeler:
        f()
    return None


# QUELS INGREDIENTS SONT REQUIS ET EN QUELLE QUANTITE ?

def ingredients_requis():
    """Renvoie une liste composée de tuples (ingrédient, quantité).
    :Exemples:
    >>> ingredients = {"patate":1.5,     # en kilogrammes
                       "échalotte":1,  # en unités
                       "huile":0       # en nombre de cuillère à soupe
                       }
    >>> ingredients_requis()
    [("patate, 1.5), ("échalotte", 1)]
    """
    global d_ingr
    l_ingr_requis = []
    for ingr in d_ingr:
        if d_ingr[ingr] != 0:
            l_ingr_requis.append((ingr, d_ingr[ingr]))
    return l_ingr_requis


# AFFICHAGE DES INGREDIENTS REQUIS, QUANTITES COMPRISES

def affiche_ingredients_requis(l_ingr_requis):
    """Affiche les ingrédients requis, quantités comprises."""
    print('\nVoici les ingrédients requis :\n')
    for ingr in l_ingr_requis:
        if ingr[0] in l_ingr_kg:
            unite = ' kg'
        elif ingr[0] in l_ingr_unit:
            unite = ''
        elif ingr[0] in l_ingr_cs:
            unite = ' c à s'
        elif ingr[0] in l_ingr_pincee:
            unite = ' pincées'
        else:
            unite = ' branches'
        print(f'- {ingr[0]:15}  {round(ingr[1], 3)}{unite}')
    return None


# FONCTION PRINCIPALE

def main_ingredients():
    presentation()
    s = saisie_de_recettes()
    l_rec_saisies = recettes_saisies(s)
    affiche_recettes_saisies(l_rec_saisies)
    l_fonctions_a_appeler = fonctions_de_recette_a_appeler(l_rec_saisies)
    appel_fonctions_de_recette(l_fonctions_a_appeler)
    l_ingr_requis = ingredients_requis()
    affiche_ingredients_requis(l_ingr_requis)

if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
    main_ingredients()
