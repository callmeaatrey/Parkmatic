# !/bin/bash

# To build the code
echo -e "\033[31m Building the binary executable of the program..."
pyinstaller --onefile --noconfirm --distpath ./ --name parking_lot ./park_matic/src/main.py

# To run the tests
echo -e "\033[32m Running the tests..."
python -m unittest discover -s ./park_matic/tests/ -p 'test_*.py'

# To run the program
echo -e "\033[33m And here comes the program. Type 'help' to get all the commands"
python park_matic/src/main.py "$1"