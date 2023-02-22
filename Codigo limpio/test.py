from main import *

import unittest


class TestingWordCountFunction(unittest.TestCase):

    def test_sorted_lists(self):
        unsorted_list = [27, 1, 9, 8, 11, 24, 5, 25, 17, 23, 26, 15, 23, 29, 28]
        sorted_list_function = ordenar_lista(unsorted_list)
        self.assertEqual(sorted_list_function, [1, 5, 8, 9, 11, 15, 17, 23, 23, 24, 25, 26, 27, 28, 29])   

    def test_str_inside_lists(self):
        unsorted_list = [27, 1, 9, 8, 11, 24, 5, 25, 17, 23, 26, 15, 23, 29, 28, 'hola']
        sorted_list_function = ordenar_lista(unsorted_list)
        self.assertEqual(sorted_list_function, "la lista debe de ser de enteros")

    def test_float_inside_lists(self):
        unsorted_list = [1, 3, 9, 10, 16, 20, 21, 22, 23, 24, 24, 26, 29, 29, 29, 10.55]
        sorted_list_function = ordenar_lista(unsorted_list)
        self.assertEqual(sorted_list_function, "la lista debe de ser de enteros")


if __name__ == '__main__':
    unittest.main()