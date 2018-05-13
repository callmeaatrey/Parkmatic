import cmd, sys

from facilities.lot import Lot
from vehicle.car import Car
from utilities.utils import Utilities


class Parkmatic(cmd.Cmd):
    """ Command line interface for the parking lot """

    if len(sys.argv) == 2:
        # Disable rawinput module use
        use_rawinput = False

        # Do not show a prompt after each command read when the input is given through a file
        prompt = ''
    else:
        prompt = '$ '

    # ----- commands ----- #
    def do_create_parking_lot(self, arg):
        'Construct the parking lot'

        global lot

        lot = Lot(int(arg))
        print 'Created a parking lot with {} slots'.format(arg)

    def do_status(self, arg):
        'Check the status of the parking lot'

        try:
            lot.show_parking_status()
        except NameError:
            print 'No parking lot found.'

    def do_park(self, arg):
        'A car turned in to the parking lot. Let\'s try to park it'

        try:
            car_details = arg.split()
            ticket_issued = lot.park(Car(car_details[0], car_details[1]))

            if ticket_issued:
                print "Allocated slot number:", ticket_issued.get_spaceid
            else:
                print "Sorry, parking lot is full"
        except NameError:
            print 'No parking lot found.'
        except IndexError:
            print 'Insufficient car details provided.'
        except:
            print 'Oops. Something went wrong'

    def do_leave(self, arg):
        'One of our customers has to leave now. Let\' say our goodbyes right'

        try:
            response = lot.unpark(int(arg))

            if response:
                print "Slot number {} is free".format(arg)
            else:
                raise IndexError
        except NameError:
            print 'No parking lot found.'
        except IndexError:
            print 'Our apologies, but we are still expanding. This slot does not exist. Let\'s try things again.'

    def do_registration_numbers_for_cars_with_colour(self, arg):
        'Gives us the registration number of the parked cars with a particular colour'

        try:
            Utilities.registration_numbers_for_cars_with_colour(lot.get_spaces, arg)
        except NameError:
            print 'No parking lot found.'

    def do_slot_numbers_for_cars_with_colour(self, arg):
        'Gives us the slot numbers for cars with a particular colour'

        try:
            Utilities.slot_numbers_for_cars_with_colour(lot.get_spaces, arg)
        except NameError:
            print 'No parking lot found.'

    def do_slot_number_for_registration_number(self, arg):
        'Gives us the slot number of a particular car'

        try:
            Utilities.slot_number_for_registration_number(lot.get_spaces, arg)
        except NameError:
            print 'No parking lot found.'

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input = open(sys.argv[1], 'rt')
        try:
            Parkmatic(stdin=input).cmdloop()
        finally:
            input.close()
    else:
        Parkmatic().cmdloop()
