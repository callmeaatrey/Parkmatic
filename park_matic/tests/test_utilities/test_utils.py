from unittest import TestCase
from park_matic.src.utilities.utils import Utilities
from park_matic.src.facilities.lot import Lot
from park_matic.src.vehicle.car import Car

class UtilsTest(TestCase):
    """ Tests for 'utils.py' """

    def setUp(self):
        super(UtilsTest, self).setUp()
        self.test_lot = Lot(5)
        self.test_car1 = Car('DL-2N-007', 'Metal Black')
        self.test_car2 = Car('DL-2N-003', 'Sapphire Red')
        self.test_car3 = Car('KA-7M-008', 'Sapphire Red')

    def tearDown(self):
        self.test_lot = Lot(5)

    def test_registration_numbers_for_cars_with_colour(self):
        """ Test for finding the registration numbers for cars with a particular colour"""

        self.test_lot.park(self.test_car1)
        self.test_lot.park(self.test_car2)
        self.test_lot.park(self.test_car3)

        self.assertEqual(
            Utilities.registration_numbers_for_cars_with_colour(self.test_lot.get_spaces, 'Sapphire Red'),
            ['DL-2N-003', 'KA-7M-008']
        )

    def test_slot_number_for_registration_number(self):
        """ Test for checking the slot number for a registration number """

        self.test_lot.park(self.test_car1)
        self.test_lot.park(self.test_car2)
        self.test_lot.park(self.test_car3)

        self.assertEqual(
            Utilities.slot_number_for_registration_number(self.test_lot.get_spaces, 'DL-2N-007'),
            1
        )

    def test_slot_numbers_for_cars_with_colour(self):
        """ Test for checking the slot numbers for cars with a particular colour """

        self.test_lot.park(self.test_car1)
        self.test_lot.park(self.test_car2)
        self.test_lot.park(self.test_car3)

        self.assertEqual(
            Utilities.slot_numbers_for_cars_with_colour(self.test_lot.get_spaces, 'Sapphire Red'),
            ['2', '3']
        )
