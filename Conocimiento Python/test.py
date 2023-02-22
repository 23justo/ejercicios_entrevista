from lib.decorators import *
from main import get_count_words

import unittest

class TestingWordCountFunction(unittest.TestCase):

    def test_wrong_param(self):    
        result = get_count_words(int(100))
        self.assertEqual(result, "Value 100 must be a String")
    
    def test_correct_param(self):
        result = get_count_words("el perro es muy grande y el gato es muy pequeño")
        self.assertNotEqual(result, "Value el perro es muy grande y el gato es muy pequeño must be a String")
    
    def test_correct_funcionality(self):
        result = get_count_words("Esto es un ejemplo Esto un un un")
        for data in result:
            if data[0] == 'Esto':
                self.assertEqual(data[1], 2)
            elif data[0] == 'es':
                self.assertEqual(data[1], 1)
            elif data[0] == 'un':
                self.assertEqual(data[1], 4)
            elif data[0] == 'ejemplo':
                self.assertEqual(data[1], 1)


if __name__ == '__main__':
    unittest.main()
