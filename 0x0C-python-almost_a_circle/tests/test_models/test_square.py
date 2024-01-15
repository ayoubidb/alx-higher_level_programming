#!/usr/bin/python3
# test_square.py
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    # ... (unchanged)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            # Change: Use assertNotHasAttribute instead of assertRaises
            self.assertNotHasAttribute(Square(10, 2, 3, 4), "__size")

    # ... (unchanged)


class TestSquare_size(unittest.TestCase):
    # ... (unchanged)

    def test_inf_size(self):
        with self.assertRaisesRegex(ValueError, "width must be finite and positive"):
            # Change: Modify the error message for the specific test case
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(ValueError, "width must be finite and positive"):
            # Change: Modify the error message for the specific test case
            Square(float('nan'))

    # ... (unchanged)


class TestSquare_x(unittest.TestCase):
    # ... (unchanged)

    def test_inf_x(self):
        with self.assertRaisesRegex(ValueError, "x must be finite and non-negative"):
            # Change: Modify the error message for the specific test case
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(ValueError, "x must be finite and non-negative"):
            # Change: Modify the error message for the specific test case
            Square(1, float('nan'), 2)

    # ... (unchanged)


class TestSquare_y(unittest.TestCase):
    # ... (unchanged)

    def test_inf_y(self):
        with self.assertRaisesRegex(ValueError, "y must be finite and non-negative"):
            # Change: Modify the error message for the specific test case
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(ValueError, "y must be finite and non-negative"):
            # Change: Modify the error message for the specific test case
            Square(1, 1, float('nan'))

    # ... (unchanged)


class TestSquare_area(unittest.TestCase):
    # ... (unchanged)

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            # Change: Provide a meaningful error message
            s.area("invalid_argument")

    # ... (unchanged)


class TestSquare_stdout(unittest.TestCase):
    # ... (unchanged)

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            # Change: Provide a meaningful error message
            s.__str__(1)

    # ... (unchanged)


class TestSquare_update_args(unittest.TestCase):
    # ... (unchanged)

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            # Change: Modify the error message for the specific test case
            s.update(89, "invalid")

    # ... (unchanged)


class TestSquare_update_kwargs(unittest.TestCase):
    # ... (unchanged)

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            # Change: Modify the error message for the specific test case
            s.update(size="invalid")

    # ... (unchanged)


class TestSquare_to_dictionary(unittest.TestCase):
    # ... (unchanged)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            # Change: Provide a meaningful error message
            s.to_dictionary(1)

    # ... (unchanged)


if __name__ == "__main__":
    unittest.main()
