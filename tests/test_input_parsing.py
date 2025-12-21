import unittest

from food_shopping_list.frontend_handler import FrontendHandler
from food_shopping_list.exceptions import InvalidInputError



class TestInputParsing(unittest.TestCase):


    def setUp(self) -> None:
        self.frontend_handler = FrontendHandler()
        self.meal_names = ['patates sautées', 'salade de patates']


    def test_get_selected_meals_from_input_returns_empty_list_when_input_is_empty(self):
        self.assertEqual([], self.frontend_handler._get_selected_meals_from_input('', self.meal_names))


    def test_get_selected_meals_from_input_returns_empty_list_when_input_is_garbage(self):
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input(' ', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input('a', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input('1a', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input('a1', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input('a 1', self.meal_names))


    def test_get_selected_meals_from_input_returns_empty_list_when_numbers_are_out_of_bound(self):
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input('0', self.meal_names))
        self.assertRaises(InvalidInputError, lambda: self.frontend_handler._get_selected_meals_from_input(f'{len(self.meal_names) + 1}', self.meal_names))


    def test_get_selected_meals_from_input_returns_the_right_meals(self):
        self.assertEqual([self.meal_names[0]], self.frontend_handler._get_selected_meals_from_input('1', self.meal_names))
        self.assertEqual([self.meal_names[0]], self.frontend_handler._get_selected_meals_from_input(' 1', self.meal_names))
        self.assertEqual([self.meal_names[0]], self.frontend_handler._get_selected_meals_from_input('1 ', self.meal_names))
        self.assertEqual([self.meal_names[0]], self.frontend_handler._get_selected_meals_from_input(' 1 ', self.meal_names))
        self.assertEqual(self.meal_names, self.frontend_handler._get_selected_meals_from_input('1 2', self.meal_names))
        self.assertEqual(self.meal_names, self.frontend_handler._get_selected_meals_from_input(' 1 2', self.meal_names))
        self.assertEqual(self.meal_names, self.frontend_handler._get_selected_meals_from_input('1 2 ', self.meal_names))
        self.assertEqual(self.meal_names, self.frontend_handler._get_selected_meals_from_input(' 1 2 ', self.meal_names))
        self.assertEqual(self.meal_names, self.frontend_handler._get_selected_meals_from_input('  1   2  ', self.meal_names))
