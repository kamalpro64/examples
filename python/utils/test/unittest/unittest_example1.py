# Reference: https://towardsdatascience.com/3-python-tools-data-scientists-can-use-for-production-quality-code-604a5e0acf9a

import math

def circle_area(radius):
    return math.pi*radius**2






import unittest

class TestFunctions(unittest.TestCase):
    def test_circle_area1(self):
        assert abs(circle_area(2) - 12.56637)

    def test_circle_area2(self):
        assert circle_area(0) == 0

unittest.main(argv=[''], verbosity=2, exit=False)
