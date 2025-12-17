# To parse and check the correctness of the file


import sys
import yaml

from food_shopping_list.exceptions import FileFormatError




def read_file(file_name: str) -> list[dict]:
    """
    Reads the file.

    Args:
        file_name: the name of the file to read

    Returns:
        The content of the file.
    """
    with open(file_name, 'r') as file:
        try:
            content: list = yaml.safe_load(file)
        except Exception as e:
            print(e)
            sys.exit(1)
    return content




def check_content_correctness(content: list) -> None:
    """
    Checks for potential errors in the content of the file.

    Args:
        content (list): the content of the file

    Raises:
        FileFormatError: if the content of the file is not correct
    """
    # check the structure
    ingredients_quantities: dict[str, list] = dict()
    for meal_dict in content:
        if not isinstance(meal_dict, dict):
            raise FileFormatError("some element of the list is not a dictionary")
        if not "meal" in meal_dict:
            raise FileFormatError("some meal's dictionary key 'meal' missing")
        if not "ingredients" in meal_dict:
            raise FileFormatError(f"{meal_dict['meal']}'s dictionary key 'ingredients' is missing")
        if not isinstance(meal_dict['ingredients'], dict):
            raise FileFormatError(f"{meal_dict['meal']}'s dictionary key 'ingredients' is not mapped to a dictionary")
        for ingredient, quantity in meal_dict['ingredients'].items():
            if not isinstance(quantity, dict):
                raise FileFormatError(f"{ingredient}'s value in meal '{meal_dict['meal']}' is not a dictionary")
            if not "quantity" in quantity:
                raise FileFormatError(f"{ingredient}'s key 'quantity' in meal '{meal_dict['meal']}' is missing")
            if not "unit" in quantity:
                raise FileFormatError(f"{ingredient}'s key 'unit' in meal '{meal_dict['meal']}' is missing")
            if ingredient not in ingredients_quantities:
                ingredients_quantities[ingredient] = []
            ingredients_quantities[ingredient].append(quantity)

    # check that the quantities of a single ingredient all use the same unit
    for ingredient, quantities in ingredients_quantities.items():
        if not len(set(quantity['unit'] for quantity in quantities)) == 1:
            raise FileFormatError(f"ingredient '{ingredient}' uses more than one unit")
