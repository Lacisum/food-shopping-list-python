# To parse and check the correctness of the file


import yaml




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
            exit(1)
    return content




def check_content_correctness(content: list) -> None:
    """
    Checks for potential errors in the content of the file.

    Args:
        content (list): the content of the file

    Raises:
        AssertionError: if the content of the file is not correct
    """
    # check the structure
    ingredients_quantities: dict[str, list] = dict()
    for meal_dict in content:
        assert isinstance(meal_dict, dict)
        assert "meal" in meal_dict
        assert "ingredients" in meal_dict
        assert isinstance(meal_dict['ingredients'], dict)
        for ingredient, quantity in meal_dict['ingredients'].items():
            assert isinstance(quantity, dict)
            assert "quantity" in quantity
            assert "unit" in quantity
            if ingredient not in ingredients_quantities:
                ingredients_quantities[ingredient] = []
            ingredients_quantities[ingredient].append(quantity)

    # check that the quantities of a single ingredient all use the same unit
    for quantities in ingredients_quantities.values():
        assert len(set(quantity['unit'] for quantity in quantities)) == 1
