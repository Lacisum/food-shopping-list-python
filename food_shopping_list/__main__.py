# This program produces a shopping (food) list for the selected meals

from pathlib import Path
import sys

from . import *




def main(argv):

    if len(argv) != 2:
        print(f'Usage: python3 -m {__package__} <file_name>')
        exit(1)

    content: list = read_file(argv[1])
    check_content_correctness(content)
    meals_dicts: list = content

    meal_names: list[str] = [meal_dict['meal'] for meal_dict in meals_dicts]

    print_presentation(meal_names)

    user_input = get_input_from_user()

    selected_meals: list[str] = get_selected_meals(user_input, meal_names)

    print_selected_meals(selected_meals)

    selected_meals_dicts = list(filter(
        lambda meal_element: meal_element['meal'] in selected_meals,
        meals_dicts
    ))

    ingredients_totals = get_ingredients_quantities(selected_meals_dicts)

    print_shopping_list(ingredients_totals)




if __name__ == '__main__':
    main(sys.argv)