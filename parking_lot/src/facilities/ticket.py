class Ticket(object):
    """A slip generated for a car when it enters the parking lot

    attributes: ticketid, spaceid
    methods: get_ticketid, get_spaceid"""

    def __init__(self, ticketid, spaceid):
        self._ticketid = ticketid
        self._spaceid = spaceid

    """ Property to get the ticket's id """
    @property
    def get_ticketid(self):
        return self._ticketid

    """ Property to get the space id in a ticket """
    @property
    def get_spaceid(self):
        return self._spaceid
