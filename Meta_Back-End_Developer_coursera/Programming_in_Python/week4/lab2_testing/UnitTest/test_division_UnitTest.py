import unittest

from division import division


class DivisionTest(unittest.TestCase):
    def test_division(self) -> None:
        self.assertEquals(division(4, 2), 2)
        self.assertEquals(division(10, 2), 5)
        self.assertEquals(division(0.009, 0.003), 3)
        self.assertRaises(ZeroDivisionError, division, 4, 0)

    def test_value(self) -> None:
        self.assertRaises(TypeError, division, "a", 2)
        self.assertRaises(TypeError, division, [4], 2)
        self.assertRaises(TypeError, division, None, None)
        self.assertEquals(division(4.4, 2), 1000)


if __name__ == "__main__":
    unittest.main()
