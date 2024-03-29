class Utilities(object):

    """ Method for finding the registration number of cars with a particular colour """
    @staticmethod
    def registration_numbers_for_cars_with_colour(spaces, colour):
        cars = []
        found = False
        for index in spaces:
            if spaces[index].get_vehicle != None:
                if spaces[index].get_vehicle.get_colour == colour:
                    found = True
                    cars.append(spaces[index].get_vehicle.get_regno)

        if not found:
            return 'Not found'
        else:
            return cars

    """ Method for finding the slot number corresponding to a registration number of a car """
    @staticmethod
    def slot_number_for_registration_number(spaces, regno):
        for index in spaces:
            if spaces[index].get_vehicle != None:
                if spaces[index].get_vehicle.get_regno == regno:
                    return spaces[index].get_spaceid

        return 'Not found'

    """ Method for finding the slot numbers for cars with a particular colour """
    @staticmethod
    def slot_numbers_for_cars_with_colour(spaces, colour):
        slots = []
        found = False
        for index in spaces:
            if spaces[index].get_vehicle != None:
                if spaces[index].get_vehicle.get_colour == colour:
                    found = True
                    slots.append(str(spaces[index].get_spaceid))

        if not found:
            return 'Not found'
        else:
            return slots
