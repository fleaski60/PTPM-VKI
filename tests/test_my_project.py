import unittest
from src.my_project import calculate_triangle


class TestMyProject(unittest.TestCase):

    def test_equilateral_triangle_with_integer_sides(self):
        t_type, coords = calculate_triangle("10", "10", "10")
        self.assertEqual(t_type, "равносторонний")

    def test_equilateral_triangle_with_float_sides(self):
        t_type, coords = calculate_triangle("5.5", "5.5", "5.5")
        self.assertEqual(t_type, "равносторонний")

    def test_isosceles_triangle_sides_a_equal_b(self):
        t_type, coords = calculate_triangle("5", "5", "8")
        self.assertEqual(t_type, "равнобедренный")

    def test_isosceles_triangle_sides_b_equal_c(self):
        t_type, coords = calculate_triangle("8", "5", "5")
        self.assertEqual(t_type, "равнобедренный")

    def test_isosceles_triangle_sides_a_equal_c(self):
        t_type, coords = calculate_triangle("5", "8", "5")
        self.assertEqual(t_type, "равнобедренный")

    def test_scalene_triangle_classic_3_4_5(self):
        t_type, coords = calculate_triangle("3", "4", "5")
        self.assertEqual(t_type, "разносторонний")
        self.assertEqual(coords, [(0, 0), (5, 0), (3, 2)])

    def test_scalene_triangle_float_values(self):
        t_type, coords = calculate_triangle("3.5", "4.5", "6.2")
        self.assertEqual(t_type, "разносторонний")

    def test_invalid_triangle_inequality_violation(self):
        t_type, coords = calculate_triangle("1", "2", "10")
        self.assertEqual(t_type, "не треугольник")
        self.assertEqual(coords, [(-1, -1), (-1, -1), (-1, -1)])

    def test_invalid_triangle_sum_equals_third_side(self):
        t_type, coords = calculate_triangle("3", "4", "7")
        self.assertEqual(t_type, "не треугольник")

    def test_negative_side_a_returns_error(self):
        t_type, coords = calculate_triangle("-5", "5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_negative_side_b_returns_error(self):
        t_type, coords = calculate_triangle("5", "-5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_negative_side_c_returns_error(self):
        t_type, coords = calculate_triangle("5", "5", "-5")
        self.assertEqual(t_type, "не треугольник")

    def test_zero_side_length_returns_error(self):
        t_type, coords = calculate_triangle("0", "5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_non_numeric_string_side_a(self):
        t_type, coords = calculate_triangle("abc", "5", "5")
        self.assertEqual(t_type, "")
        self.assertEqual(coords, [(-2, -2), (-2, -2), (-2, -2)])

    def test_non_numeric_string_side_b(self):
        t_type, coords = calculate_triangle("5", "xyz", "5")
        self.assertEqual(t_type, "")

    def test_non_numeric_string_side_c(self):
        t_type, coords = calculate_triangle("5", "5", "hello")
        self.assertEqual(t_type, "")

    def test_empty_string_input(self):
        t_type, coords = calculate_triangle("", "", "")
        self.assertEqual(t_type, "")

    def test_none_input_handled_gracefully(self):
        t_type, coords = calculate_triangle(None, "5", "5")
        self.assertEqual(t_type, "")

    def test_string_numeric_with_spaces(self):
        t_type, coords = calculate_triangle(" 10 ", " 10 ", " 10 ")
        self.assertEqual(t_type, "равносторонний")

    def test_large_numbers_input(self):
        t_type, coords = calculate_triangle("100", "100", "100")
        self.assertEqual(t_type, "равносторонний")


if __name__ == "__main__":
    unittest.main()