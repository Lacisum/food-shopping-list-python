# To check what meals have been selected by the user


import re




def get_selected_meals(user_input: str, meal_names: list[str]) -> list[str]:
    """
    Returns the list of meals selected by the user

    Args:
        user_input (str): the string that the user typed
        meal_names (list[str]): the list of all meals

    Returns:
        list[str]: the list of meals selected by the user

    Examples :
    >>> get_selected_meals('1', ['salade de patates', 'patates sautées'])
    ['salade de patates']
    >>> get_selected_meals('2', ['salade de patates', 'patates sautées'])
    ['patates sautées']
    >>> get_selected_meals('1 2', ['salade de patates', 'patates sautées'])
    ['salade de patates', 'patates sautées']
    >>> get_selected_meals('', ['salade de patates', 'patates sautées'])
    []
    >>> get_selected_meals('Lorem ipsum', ['salade de patates', 'patates sautées'])
    []
    """
    selected_meals = []
    if re.fullmatch(r'( *(\d+) *)+', user_input):
        the_numbers = re.findall(r'\d+', user_input)
        # remove duplicates
        the_numbers = set(the_numbers)
        # convert from strings to ints
        the_numbers = list(map(lambda n: int(n), the_numbers))
        # sort
        the_numbers.sort()
        # filter
        the_numbers = list(filter(lambda n: n > 0 and n < len(meal_names) + 1, the_numbers))
        for n in the_numbers:
            selected_meals.append(meal_names[n-1])
    return selected_meals




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
