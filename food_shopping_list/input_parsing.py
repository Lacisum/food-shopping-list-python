# To check what meals have been selected by the user


import re

from food_shopping_list.InvalidInputError import InvalidInputError




def get_selected_meals(user_input: str, meal_names: list[str]) -> list[str]:
    """
    Returns the list of meals selected by the user

    Args:
        user_input (str): the string that the user typed
        meal_names (list[str]): the list of all meals

    Returns:
        list[str]: the list of meals selected by the user

    Raises:
        InvalidInputError: if the user input is not an empty string, or is not
            made of integers separated by spaces, or if the integers are not
            part of those proposed

    Examples :
    >>> get_selected_meals('1', ['salade de patates', 'patates sautées'])
    ['salade de patates']
    >>> get_selected_meals('2', ['salade de patates', 'patates sautées'])
    ['patates sautées']
    >>> get_selected_meals('1 2', ['salade de patates', 'patates sautées'])
    ['salade de patates', 'patates sautées']
    >>> get_selected_meals('', ['salade de patates', 'patates sautées'])
    []
    """
    if not re.fullmatch(r'( *(\d+) *)*', user_input):
        raise InvalidInputError('The input must be integers separated by spaces.')
    the_numbers = re.findall(r'\d+', user_input)
    if len(the_numbers) == 0:
        return []
    # remove duplicates
    the_numbers = list(set(the_numbers))
    # convert from strings to ints
    the_numbers = list(map(lambda n: int(n), the_numbers))
    # sort
    the_numbers.sort()
    # refuse out of bound numbers
    if the_numbers[0] <= 0 or the_numbers[-1] > len(meal_names):
        raise InvalidInputError('The numbers must be part of those proposed.')
    # return the meals names associated to the numbers
    return [meal_names[n-1] for n in the_numbers]




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
