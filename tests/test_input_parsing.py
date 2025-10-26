import unittest

from food_shopping_list.input_parsing import get_selected_meals
from food_shopping_list.exceptions import InvalidInputError



class TestInputParsing(unittest.TestCase):


    def setUp(self) -> None:
        self.meal_names = ['patates sautées', 'salade de patates']


    def test_get_selected_meals_returns_empty_list_when_input_is_empty(self):
        self.assertEqual([], get_selected_meals('', self.meal_names))


    def test_get_selected_meals_returns_empty_list_when_input_is_garbage(self):
        self.assertRaises(InvalidInputError, lambda: get_selected_meals(' ', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: get_selected_meals('a', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: get_selected_meals('1a', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: get_selected_meals('a1', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: get_selected_meals('a 1', self.meal_names))


    def test_get_selected_meals_returns_empty_list_when_numbers_are_out_of_bound(self):
        self.assertRaises(InvalidInputError, lambda: get_selected_meals('0', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: get_selected_meals(f'{len(self.meal_names) + 1}', self.meal_names))


    def test_get_selected_meals_returns_the_right_meals(self):
        self.assertEqual([self.meal_names[0]], get_selected_meals('1', self.meal_names))
        self.assertEqual([self.meal_names[0]], get_selected_meals(' 1', self.meal_names))
        self.assertEqual([self.meal_names[0]], get_selected_meals('1 ', self.meal_names))
        self.assertEqual([self.meal_names[0]], get_selected_meals(' 1 ', self.meal_names))
        self.assertEqual(self.meal_names, get_selected_meals('1 2', self.meal_names))
        self.assertEqual(self.meal_names, get_selected_meals(' 1 2', self.meal_names))
        self.assertEqual(self.meal_names, get_selected_meals('1 2 ', self.meal_names))
        self.assertEqual(self.meal_names, get_selected_meals(' 1 2 ', self.meal_names))
        self.assertEqual(self.meal_names, get_selected_meals('  1   2  ', self.meal_names))
