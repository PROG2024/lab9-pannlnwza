"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        """Creates circle before test."""
        self.circle = Circle(1)
        self.circle1 = Circle(2)
        self.circle_edge_case = Circle(0)

    def test_add_area(self):
        """Test for add_area using typical values."""
        expected_radius = (self.circle.get_radius()**2 + self.circle1.get_radius()**2)**0.5
        self.assertEqual(expected_radius, self.circle.add_area(self.circle1).radius)
        expected_area = Circle(expected_radius).get_area()
        self.assertEqual(expected_area, self.circle.add_area(self.circle1).get_area())

    def test_add_area_edge_case(self):
        """Test for add_area for an "edge case" where one circle has radius 0."""
        expected_radius = (self.circle_edge_case.get_radius() ** 2 + self.circle.get_radius() ** 2) ** 0.5
        self.assertEqual(expected_radius, self.circle_edge_case.add_area(self.circle).radius)
        expected_area = Circle(expected_radius).get_area()
        self.assertEqual(expected_area, self.circle_edge_case.add_area(self.circle).get_area())

    def test_negative_radius(self):
        """Test that circle constructor raises exception of radius is negative."""
        with self.assertRaises(ValueError):
            Circle(-1)