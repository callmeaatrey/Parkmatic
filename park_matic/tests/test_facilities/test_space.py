from unittest import TestCase
from park_matic.src.facilities.space import Space
from park_matic.src.vehicle.car import Car


class SpaceTest(TestCase):
    """ Tests for 'space.py' """

    def setUp(self):
        super(SpaceTest, self).setUp()
        self.test_space = Space('1')

    def test_get_spaceid(self):
        """ Test for checking the space's id """

        self.assertEqual(self.test_space.get_spaceid, '1')

    def test_car_park(self):
        """ Test for checking when parking a car """

        self.test_space.park(Car("DL-2N-007", "Space Grey"))

        self.assertEqual(self.test_space.get_vehicle.get_regno, 'DL-2N-007')
        self.assertEqual(self.test_space.get_vehicle.get_colour, 'Space Grey')

    def test_car_unpark(self):
        """ Test for checking when unparking a car """

        self.test_space.park(Car("DL-2N-007", "Space Grey"))

        self.assertEqual(self.test_space.get_vehicle.get_regno, 'DL-2N-007')
        self.assertEqual(self.test_space.get_vehicle.get_colour, 'Space Grey')

        self.test_space.unpark()

        self.assertEqual(self.test_space.get_vehicle, None)