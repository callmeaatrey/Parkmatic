from unittest import TestCase
from parking_lot.src.facilities.lot import Lot
from parking_lot.src.vehicle.car import Car

class LotTest(TestCase):
    """ Tests for 'lot.py' """

    def setUp(self):
        super(LotTest, self).setUp()
        self.test_lot = Lot(7)

    def tearDown(self):
        self.test_lot = Lot(7)

    def test_total_available_spaces(self):
        """ Test for checking the total available spaces """

        self.assertEqual(self.test_lot.get_total_spaces, 7)

    def test_ticket_count_increment(self):
        """ Test for checking the ticket counter increment """

        self.test_lot.set_ticket_count(1)

        self.assertEqual(self.test_lot.get_ticket_count, 1)

    def test_park_a_car(self):
        """ Test for parking a car """

        self.test_lot.park(Car('DL-2N-007', 'Rose Gold'))

        self.assertEqual(self.test_lot.get_ticket_count, 1)
        self.assertEqual(self.test_lot.get_spaces[1].get_vehicle.get_regno, 'DL-2N-007')
        self.assertEqual(self.test_lot.get_spaces[1].get_vehicle.get_colour, 'Rose Gold')

    def test_unpark_a_car(self):
        """ Test for unparking a car """

        self.test_lot.park(Car('DL-2N-007', 'Rose Gold'))

        self.assertEqual(self.test_lot.get_ticket_count, 1)
        self.assertEqual(self.test_lot.get_spaces[1].get_vehicle.get_regno, 'DL-2N-007')
        self.assertEqual(self.test_lot.get_spaces[1].get_vehicle.get_colour, 'Rose Gold')

        self.test_lot.unpark(1)
        self.assertEqual(self.test_lot.get_spaces[1].get_vehicle, None)
