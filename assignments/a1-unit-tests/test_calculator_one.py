from unittest import TestCase
from calculator_one import Calculator

class TestCalculator(TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_default_init_calculation(self):
        actual = self.calculator.get_last_calculation()
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 0
        self.assertEqual(actual, expected, "Default should be zero")

    def test_invalid_init_parameter_type(self):
        with self.assertRaises(ValueError, msg="Invalid Output: non integer parameter"):
            self.calculator = Calculator(tuple())

    def test_valid_init_parameter_type(self):
        self.calculator = Calculator(10)
        actual = self.calculator.get_last_calculation()
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 10
        self.assertEqual(actual, expected, "Init parameter 10 should match the latest calculation")

    def test_default_operand_for_add_to_last_calculation(self):
        self.calculator = Calculator(5)
        actual = self.calculator.add_to_last_calculation()
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 5
        self.assertEqual(actual, expected, "Invalid Output: expected to have 0 added to the initial value")

    def test_invalid_operand_for_add_to_last_calculation(self):
        with self.assertRaises(ValueError, msg="Invalid Output: non integer parameter"):
            self.calculator.add_to_last_calculation(list())

    def test_valid_operand_for_add_to_last_calculation(self):
        self.calculator = Calculator(5)
        actual = self.calculator.add_to_last_calculation(3)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 8
        self.assertEqual(actual, expected, "Invalid Output: expected to have 3 added to the initial value")

    def test_default_operand_for_subtract_from_last_calculation(self):
        self.calculator = Calculator(5)
        actual = self.calculator.subtract_from_last_calculation()
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 5
        self.assertEqual(actual, expected, "Invalid Output: expected to have 0 subtracted to the initial value")

    def test_invalid_operand_for_subtract_from_last_calculation(self):
        with self.assertRaises(ValueError, msg="Invalid Output: non integer parameter"):
            self.calculator.subtract_from_last_calculation(list())

    def test_valid_operand_for_subtract_from_last_calculation(self):
        self.calculator = Calculator(5)
        actual = self.calculator.subtract_from_last_calculation(3)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 2
        self.assertEqual(actual, expected, "Invalid Output: expected to have 2 subtracted to the initial value")

    def test_default_operand_two_add_parameter(self):
        actual = self.calculator.add(7)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 7
        self.assertEqual(actual, expected, "Invalid Output: expected to have 7 added to the default value")

    def test_invalid_add_parameters(self):
        with self.assertRaises(ValueError, msg="Invalid Output: non integer parameters"):
            self.calculator.add(dict(), set())

    def test_valid_add_parameters(self):
        actual = self.calculator.add(3, 2)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 5
        self.assertEqual(actual, expected, "Invalid Output: expected addition calculation to have 5")

    def test_default_operand_two_subtract_parameter(self):
        actual = self.calculator.subtract(7)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 7
        self.assertEqual(actual, expected, "Invalid Output: expected to have 7 subtracted to the default value")

    def test_invalid_subtract_parameters(self):
        with self.assertRaises(ValueError, msg="Invalid Output: non integer parameters"):
            self.calculator.subtract(dict(), set())

    def test_valid_subtract_parameters(self):
        actual = self.calculator.subtract(3, 2)
        if type(actual) != int:
            self.fail("actual was not a number data type: int, float, or complex")
        expected = 1
        self.assertEqual(actual, expected, "Invalid Output: expected subtraction calculation to have 1")
