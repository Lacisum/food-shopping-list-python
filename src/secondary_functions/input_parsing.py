# To check what meals have been selected by the user


import re




def get_selected_meals(user_input: str, meal_names: list[str]) -> list[str]:
    """
    Returns the list of meals typed by the user

    Args:
        user_input (str): the string that the user typed
        meal_names (list[str]): the list of all meals

    Returns:
        list[str]: the list of meals typed by the user

    Examples :
    >>> get_entered_meals('salade de patates', ['salade de patates', 'patates sautées'])
    ['salade de patates']
    >>> get_entered_meals('salade de patates blablabla patates sautées', ['salade de patates', 'patates sautées'])
    ['salade de patates', 'patates sautées']
    >>> get_entered_meals('patates sautees', ['salade de patates', 'patates sautées'])
    []
    >>> get_entered_meals('canapé', ['salade de patates', 'patates sautées'])
    []
    """
    return [meal for meal in meal_names if _meal_is_entered(user_input, meal)]




def _meal_is_entered(user_input: str, meal_name: str) -> bool:
    """
    Checks if the given meal name is present in the given input.

    Args:
        input (str): the input of the user
        meal_name (str): the name of a meal

    Returns:
        bool: True if the given meal name is present in the given input, else False

    Examples :
    >>> meal_is_entered('patates sautées', 'je veux des patates sautées  ')
    True
    >>> meal_is_entered('patates sautées', 'patates sautees')
    False
    """
    return bool(re.search(meal_name, user_input))




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
