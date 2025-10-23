# To compute the total quantities of the ingredients of the selected meals




def get_ingredients_quantities(selected_meals_dicts: list[dict]) -> dict:
    """
    Returns a dictionary that associates each ingredient with the sum of its
    quantities across the selected meals.

    Args:
        selected_meals (list[dict]): the list of meals selected by the user

    Returns:
        A dictionary that associates each ingredient with its total quantity.
    """
    # build a dictionary that associates each ingredient with the list of its quantities
    ingredients_quantities: dict[str, list] = dict()
    for meal_dict in selected_meals_dicts:
        for ingredient, quantity in meal_dict['ingredients'].items():
            if ingredient not in ingredients_quantities:
                ingredients_quantities[ingredient] = []
            ingredients_quantities[ingredient].append(quantity)

    # sum the quantities of each ingredient
    ingredients_totals = dict()
    for ingredient, quantities in ingredients_quantities.items():
        total_quantity = {
            "quantity": _sum_ingredient_quantities(quantities),
            "unit": quantities[0]['unit']
        }
        ingredients_totals[ingredient] = total_quantity

    return ingredients_totals




def _sum_ingredient_quantities(quantities: list[dict]) -> int|float:
    """
    Returns the sum of the given quantities

    If the result is a float:
    - if it equals an integer, converts it to an integer;
    - otherwise, it is rounded to 3 digits after the comma.

    Args:
        quantities (list[dict]): the quantities

    Returns:
        int|float: the sum of the quantities
    """
    res = sum([quantity['quantity'] for quantity in quantities])
    if isinstance(res, int):
        return res
    res = round(res, 3)
    if res == int(res):
        res = int(res)
    return res
