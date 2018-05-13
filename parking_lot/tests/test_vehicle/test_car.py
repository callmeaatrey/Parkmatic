from unittest import TestCase
from parking_lot.src.vehicle.car import Car


class CarTest(TestCase):
    """ Tests for 'car.py' """

    def setUp(self):
        super(CarTest, self).setUp()
        self.test_car = Car('DL-2N-007', 'Space Grey')

    def test_regno(self):
        """ Test for checking the regustration number """

        self.assertEqual(self.test_car.get_regno, 'DL-2N-007')

    def test_colour(self):
        """ Test for checking the colour of the car """

        self.assertEqual(self.test_car.get_colour, 'Space Grey')
