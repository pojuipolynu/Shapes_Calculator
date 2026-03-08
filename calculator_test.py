import unittest

from calculator import shape_clasificator


class TestCalculations(unittest.TestCase):

    def test_value_error(self):
        value_error_data = "square topright 1 1 side 1 rectangle topright 2 2 bottomleft 1 1 circle center 1 1 radius q"
        value_error_result = "Square Perimeter 4.0 Area 1.0\nRectangle Perimeter 4.0 Area 1.0\nInput data is invalid\n"

        result = shape_clasificator(value_error_data)
        self.assertEqual(result, value_error_result)

    def test_index_error(self):
        index_error_data = "square topright 1 1 side 1 rectangle topright 2 2 bottomleft 1 1 circle center 1 1 radius"
        index_error_result = "Square Perimeter 4.0 Area 1.0\nRectangle Perimeter 4.0 Area 1.0\nNot enough data\n"

        result = shape_clasificator(index_error_data)
        self.assertEqual(result, index_error_result)

    def test_right_input(self):
        right_input_data = "square topright 1 1 side 1 rectangle topright 2 2 bottomleft 1 1 circle center 1 1 radius 2"
        right_input_result = "Square Perimeter 4.0 Area 1.0\nRectangle Perimeter 4.0 Area 1.0\nCircle Perimeter 12.56 Area 12.56\n"

        result = shape_clasificator(right_input_data)
        self.assertEqual(result, right_input_result)

if __name__ == "__main__":
    unittest.main()