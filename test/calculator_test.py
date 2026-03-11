import unittest
from utils.utils_functions import shape_clasificator
from utils.key_words_class import key_words

class TestCalculations(unittest.TestCase):

    def test_right_input(self):
        right_input = "square side 1 rectangle topright 2 2 bottomleft 1 1 circle radius 2"
        right_result = (
            "Square Perimeter 4.0 Area 1.0\n"
            "Rectangle Perimeter 4.0 Area 1.0\n"
            "Circle Perimeter 12.56 Area 12.56\n"
        )
        result = shape_clasificator(right_input)
        self.assertEqual(result, right_result)

    def test_value_error(self):
        value_error_input = "square side 1 circle radius q"
        value_error_result = key_words.valueerror
        result = shape_clasificator(value_error_input)
        self.assertEqual(result, value_error_result)

    def test_index_error(self):
        index_error_input = "square side 1 circle radius"
        index_error_result = key_words.indexerror
        result = shape_clasificator(index_error_input)
        self.assertEqual(result, index_error_result)

if __name__ == "__main__":
    unittest.main()