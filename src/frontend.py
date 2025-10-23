# For displaying




def print_presentation(meal_names: list) -> None:
    """
    Prints the presentation of the program, including the list of meals.

    Args:
        meal_names (list): the list of meals names
    """
    print()
    print('Ce programme te donne la liste des ingrédients requis pour réaliser les recettes que tu choisis.\n')
    print('Voici la liste des recettes disponibles :')
    for meal in meal_names:
        print(f"- {meal}")
    print()




def get_input_from_user() -> str:
    """Prompts the user to type one or more meals names."""
    print('Saisis la/les recette(s) que tu veux réaliser.')
    user_input = input()
    print()
    return user_input




def print_selected_meals(selected_meals: list[str]) -> None:
    """
    Prints the meals selected by the user.

    Args:
        selected_meals (list[str]): the selected meals    
    """
    print('Tu as saisi les recettes suivantes :')
    for meal in selected_meals:
        print(f'- {meal}')
    print()




def print_shopping_list(ingredients_totals: dict[str, dict]) -> None:
    """
    Prints the shopping list.

    Args:
        ingredients_totals (dict[str, dict]): a dictionary that associates each
            needed ingredient to its quantity
    """
    print('Voici tous les ingrédients requis :')
    max_ingr_name_length = max(map(
        lambda ingr_name : len(ingr_name),
        ingredients_totals.keys()
    ))
    for ingredient, quantity in ingredients_totals.items():
        _print_shopping_list_line(max_ingr_name_length, ingredient, quantity)




def _print_shopping_list_line(
        max_ingr_name_length: int,
        ingredient: str,
        quantity: dict[str, int|float]
    ) -> None:
    """
    Prints a line where the given ingredient is shown with its quantity.

    Args:
        max_ingr_name_length (int): the maximum length of the ingredients' names
        ingredient (str): the name of the ingredient
        quantity (dict[str, int|float]): a dictionary containg the quantity (with unit) of the ingredient
    """
    print('- {}{} {}'.format(
        ingredient.ljust(max_ingr_name_length+4, '.'),
        quantity['quantity'],
        quantity['unit']
    ))
