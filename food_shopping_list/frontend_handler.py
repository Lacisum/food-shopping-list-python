# For displaying

import re
import sys

from food_shopping_list.exceptions import FileFormatError, InvalidInputError




class FrontendHandler:
    """A class for interfacing with the user."""

    def print_usage(self) -> None:
        """Prints the usage of the program."""
        print(f'Usage: python3 -m {__package__} <file_name>')




    def print_meals_file_error(self, file_name: str, exception: FileFormatError) -> None:
        """
        Prints an error that's in the meals file.

        Args:
            file_name (str): the name of the meals file
            exception (str): the raised AssertionError
        """
        print(f"Error in {file_name}: {exception}", file=sys.stderr)




    def print_available_meals(self, meal_names: list[str]) -> None:
        """
        Prints the list of available meals.

        Args:
            meal_names (list): the list of meals names
        """
        print()
        print('Available meals:')
        for i in range(len(meal_names)):
            print(f"{i+1}. {meal_names[i]}")
        print()




    def get_selected_meals(self, meal_names: list[str]) -> list[str]:
        """Gets the meals selected by the user.

        Returns:
            list[str]: the list of meal names the user selected
        """
        user_input: str = self._prompt_user_input('Enter the numbers of the meals you want to make, separating them with a space:')
        input_is_correct = False
        while not input_is_correct:
            try:
                selected_meals: list[str] = self._get_selected_meals_from_input(user_input, meal_names)
                input_is_correct = True
            except InvalidInputError as e:
                user_input = self._prompt_user_input(f'{e.message}\r\nPlease try again:')
        return selected_meals




    def print_you_didnt_choose_any_meal(self, ) -> None:
        """Prints a message that tells the user they didn't choose any meal."""
        print("You didn't choose any meal.")




    def print_selected_meals(self, selected_meals: list[str]) -> None:
        """
        Prints the meals selected by the user.

        Args:
            selected_meals (list[str]): the selected meals    
        """
        print('You chose the following meals:')
        for meal in selected_meals:
            print(f'- {meal}')
        print()




    def print_shopping_list(self, ingredients_totals: dict[str, dict]) -> None:
        """
        Prints the shopping list.

        Args:
            ingredients_totals (dict[str, dict]): a dictionary that associates each
                needed ingredient to its quantity
        """
        print('Here are the required ingredients:')
        max_ingr_name_length = max(map(
            lambda ingr_name : len(ingr_name),
            ingredients_totals.keys()
        ))
        for ingredient, quantity in ingredients_totals.items():
            self._print_shopping_list_line(max_ingr_name_length, ingredient, quantity)




    def _get_selected_meals_from_input(self, user_input: str, meal_names: list[str]) -> list[str]:
        """Parses the provided input for meal numbers and returns the list of corresponding meals.

        Args:
            input (str): the raw user input
            meal_names (list[str]): the list of available meals

        Returns:
            list[str]: the names of the user-selected meals

        Raises:
            InvalidInputError: if the user input is not an empty string, or is
                not made of integers separated by spaces, or if the integers are
                not part of those proposed

        Examples :
        >>> frontend_handler = FrontendHandler()
        >>> frontend_handler._get_selected_meals_from_input('1', ['salade de patates', 'patates sautées'])
        ['salade de patates']
        >>> frontend_handler._get_selected_meals_from_input('2', ['salade de patates', 'patates sautées'])
        ['patates sautées']
        >>> frontend_handler._get_selected_meals_from_input('1 2', ['salade de patates', 'patates sautées'])
        ['salade de patates', 'patates sautées']
        >>> frontend_handler._get_selected_meals_from_input('', ['salade de patates', 'patates sautées'])
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




    def _prompt_user_input(self, message: str) -> str:
        """Prompts the user to type the numbers of the meals they want to prepare.

        Args:
            message (str): the message to prompt the user with

        Returns:
            str: the raw user input
        """
        print(message)
        user_input: str = input()
        print()
        return user_input




    def _print_shopping_list_line(
            self,
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




if __name__ =='__main__':
    # Run with : python -m food_shopping_list.frontend_handler
    import doctest
    doctest.testmod(verbose=True)
