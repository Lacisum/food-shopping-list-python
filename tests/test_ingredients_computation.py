import unittest

from food_shopping_list.ingredients_computation import get_ingredients_quantities




class TestIngredientsComputation(unittest.TestCase):


    def test_get_ingredients_quantities_when_input_is_empty(self):
        input = []
        expected = {}
        self.assertEqual(expected, get_ingredients_quantities(input))


    def test_get_ingredients_quantities_when_input_has_round_total_quantity(self):
        input = [
            {
                'meal': 'patates sautées',
                'ingredients': {
                    'patates': {
                        'quantity': 0.5,
                        'unit': 'kg'
                    }
                }
            },
            {
                'meal': 'purée',
                'ingredients': {
                    'patates': {
                        'quantity': 0.5,
                        'unit': 'kg'
                    }
                }
            }
        ]
        expected = {'patates': {'quantity': 1, 'unit': 'kg'}}
        self.assertEqual(expected, get_ingredients_quantities(input))


    def test_get_ingredients_quantities_when_input_has_float_total_quantity(self):
        input = [
            {
                'meal': 'patates sautées',
                'ingredients': {
                    'patates': {
                        'quantity': 0.6,
                        'unit': 'kg'
                    }
                }
            },
            {
                'meal': 'purée',
                'ingredients': {
                    'patates': {
                        'quantity': 0.7,
                        'unit': 'kg'
                    }
                }
            }
        ]
        expected = {'patates': {'quantity': 1.3, 'unit': 'kg'}}
        self.assertEqual(expected, get_ingredients_quantities(input))
