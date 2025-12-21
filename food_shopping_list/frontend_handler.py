# For displaying

import sys

from food_shopping_list.exceptions import FileFormatError




class FrontendHandler:

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




    def print_available_meals(self, meal_names: list) -> None:
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




    def prompt_user_input(self) -> None:
        """Prompts the user to type the numbers of the meals they want to prepare."""
        print('Enter the numbers of the meals you want to make, separating them with a space:')




    def prompt_user_input_again(self, exception_message: str) -> None:
        """
        Prompts the user to type the numbers of the meals they want to prepare (again).
        Assumes that the user has already tried to input something before and that their input was incorrect.

        Args:
            exception_message (str): the message of the exception that occured during the previous input trial
        """
        print(exception_message)
        print('Please try again:')




    def print_you_didnt_chose_any_meal(self, ) -> None:
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
