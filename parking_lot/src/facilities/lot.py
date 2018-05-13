from space import Space
from ticket import Ticket


class Lot(object):
    """A place to park your cars

    attributes: ticket_count, total_spaces, spaces"""

    def __init__(self, spaces):
        self._ticket_count = 0
        self._total_spaces = spaces
        self._spaces = {}

        for index in range(1, self._total_spaces + 1):
            self._spaces[index] = Space(index)

    """ Property to get the parking lot's total spaces """
    @property
    def get_total_spaces(self):
        return self._total_spaces

    """ Property to get the total tickets issued so far """
    @property
    def get_ticket_count(self):
        return self._ticket_count

    """ Property to get the parking space's data """
    @property
    def get_spaces(self):
        return self._spaces

    """ Method to increase the ticket count """
    def set_ticket_count(self, count):
        self._ticket_count = count

    """ Method to check the status of the parking lot """
    def show_parking_status(self):
        values = self.get_spaces.values()

        print "Slot No.  Registration No.  Colour"
        for index in range(len(values)):
            if values[index].get_vehicle:
                print '{}  {}  {}'.format(values[index].get_spaceid, values[index].get_vehicle.get_regno, values[index].get_vehicle.get_colour)

    """ Method to get the available empty slots """
    def get_empty_slots(self):
        return [index + 1 for index in range(len(self.get_spaces.values())) if not self.get_spaces[index + 1].get_vehicle]

    """ Method to check if a new car can find a parking space """
    def can_park(self):
        if not self.get_empty_slots():
            return False
        else:
            return True

    """ Method to see where to park """
    def where_to_park(self):
        empty_slots = self.get_empty_slots()
        if not empty_slots:
            return -1
        else:
            return empty_slots[0]

    """ Method to invoke when a new car is to be parked """
    def park(self, vehicle):
        if not self.can_park():
            return False

        slot = self.where_to_park()
        self.set_ticket_count(self.get_ticket_count + 1)
        ticket_to_issue = Ticket(self.get_ticket_count, slot)
        if slot != -1:
            space = self._spaces[slot]
            space.park(vehicle)

        return ticket_to_issue

    """ Method to invoke when a park has to be unparked """
    def unpark(self, slot):
        if slot not in range(1, self.get_total_spaces + 1):
            return False

        space = self._spaces[slot]
        space.unpark()

        return True
