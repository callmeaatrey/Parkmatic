class Space(object):
    """A location that is designated for parking

    attributes: space id, vehicle
    methods: get_vehicle, get_spaceid, park, unpark"""

    def __init__(self, spaceid):
        self._spaceid = spaceid
        self._vehicle = None

    """ Property to get the parking space's vehicle details """
    @property
    def get_vehicle(self):
        return self._vehicle

    """ Property to get the parking space's id """
    @property
    def get_spaceid(self):
        return self._spaceid

    """ Method to park a car """
    def park(self, vehicle):
        self._vehicle = vehicle

    """ Method to unpark a car """
    def unpark(self):
        self._vehicle = None
