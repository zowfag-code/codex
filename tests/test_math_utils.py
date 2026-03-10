import unittest

from src.math_utils import add, is_even


class MathUtilsTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_is_even_true(self) -> None:
        self.assertTrue(is_even(10))

    def test_is_even_false(self) -> None:
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()
