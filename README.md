# Parkmatic

One stop for all your parking needs. And surprisingly there are no humans involved.

> _I visualize a time when we will be to robots what dogs are to humans, and I’m rooting for the machines._

### Prerequisites and Running the Program

Just clone the repository and you get two major commands to perform:

1. For running the program:
```
./parking_lot <<input_file>>
```
If the input_file path is not provided, then an interactive shell opens up and you can use the following commands:

+ _create_parking_lot_
+ _status_
+ _registration_numbers_for_cars_with_colour_
+ _slot_number_for_registration_number_
+ _slot_numbers_for_cars_with_colour_
+ _park_
+ _leave_

2. If you want to make a build, run the tests and then launch the program, then enter the following commands:

```
source .bashrc
parking_lot
```
**NOTE**: To make the build process successfull, you need `pyinstaller` which you can easily install using the command:

```
pip install pyinstaller
```

## Running the tests

To run the tests on the code, enter the following command from the root of the root of the directory:

```
python -m unittest discover -s ./park_matic/tests/ -p 'test_*.py'
```
## Built With

* Python 2.7

## Authors

* **Shikher Aatrey**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details