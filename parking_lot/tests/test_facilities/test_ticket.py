from unittest import TestCase
from parking_lot.src.facilities.ticket import Ticket

class TicketTest(TestCase):
    """ Tests for 'ticket.py' """

    def setUp(self):
        super(TicketTest, self).setUp()
        self.test_ticket = Ticket('001', '1')

    def test_ticketid(self):
        """ Test for checking the ticket id """

        self.assertEqual(self.test_ticket.get_ticketid, '001')

    def test_spaceid_on_ticket(self):
        """ test for checking the space id on ticket """

        self.assertEqual(self.test_ticket.get_spaceid, '1')
