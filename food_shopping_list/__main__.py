# This program produces a shopping (food) list for the selected meals


import sys

from . import *




def main(argv):

    if len(argv) != 2:
        print_usage()
        exit(1)

    file_name = argv[1]

    content: list = read_file(file_name)

    try:
        check_content_correctness(content)
    except AssertionError as e:
        print_meals_file_error(file_name, e)
        exit(1)

    meals_dicts: list = content

    meal_names: list[str] = [meal_dict['meal'] for meal_dict in meals_dicts]

    print_available_meals(meal_names)

    prompt_user_input()
    user_input = input()
    print()
    input_is_correct = False
    while not input_is_correct:
        try:
            selected_meals: list[str] = get_selected_meals(user_input, meal_names)
            input_is_correct = True
        except InvalidInputError as e:
            prompt_user_input_again(e.message)
            user_input = input()
            print()

    if not selected_meals:
        print_you_didnt_chose_any_meal()
        return

    print_selected_meals(selected_meals)

    selected_meals_dicts = list(filter(
        lambda meal_element: meal_element['meal'] in selected_meals,
        meals_dicts
    ))

    ingredients_totals = get_ingredients_quantities(selected_meals_dicts)

    print_shopping_list(ingredients_totals)




if __name__ == '__main__':
    main(sys.argv)