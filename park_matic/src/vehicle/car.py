class Car(object):
    """There is a metal-body beast desperate for a parking spot. Let's hope we can find it one!

    attributes: registration number, colour
    methods: get_regno, get_colour"""

    def __init__(self, regno, colour):
        self._regno = regno
        self._colour = colour

    """ Property to get the car's registration number """
    @property
    def get_regno(self):
        return self._regno

    """ Property to get the car's colour """
    @property
    def get_colour(self):
        return self._colour
