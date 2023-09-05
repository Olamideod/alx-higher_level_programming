 Project: Python and C Scripts

This project contains a set of Python and C scripts that perform various tasks. Below are the details of each task and how to run them.
 Task 0: Run Python file

**Description**: Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

**Usage**:
export PYFILE=main.py  # Set the PYFILE environment variable to your Python script's filename
./0-run  # Run the shell script

Task 1: Run inline
Description: Write a Shell script that runs Python code. The Python code will be saved in the environment variable $PYCODE.

Task 2: Hello, print
Description: Write a Python script that prints exactly "Programming is like building a multilingual puzzle," followed by a new line.

Task 3: Print integer
Description: Complete this source code to print the integer stored in the variable number, followed by " Battery street," followed by a new line.

Task 4: Print float
Description: Complete the source code to print the float stored in the variable number with a precision of 2 digits.

Task 5: Print string
Description: Complete this source code to print 3 times a string stored in the variable str, followed by its first 9 characters.

Task 6: Play with strings
Description: Complete this source code to print "Welcome to Holberton School!"

Task 7: Copy - Cut - Paste
Description: Complete this source code to manipulate a string variable

Task 8: Create a new sentence
Description: Complete this source code to print "object-oriented programming with Python," followed by a new line.

Usage:

bash
Copy code
./8-concat_edges.py

Task 9: Easter Egg
Description: Write a Python script that prints "The Zen of Python," by Tim Peters, followed by a new line.

Usage:

bash
Copy code
./9-easter_egg.py

Task 10: Linked list cycle
Description: Write a C function that checks if a singly linked list has a cycle in it.

Usage:

c
Copy code
int check_cycle(listint_t *list);

Task 11: Hello, write (Advanced)
Description: Write a Python script that prints a specific message to stderr and exits with a status code of 1.

Usage:

bash
Copy code
./100-write.py

Task 12: Compile (Advanced)
Description: Write a script that compiles a Python script file. The Python file name will be stored in the environment variable $PYFILE.

Usage:

bash
Copy code
export PYFILE=main.py  # Set the PYFILE environment variable to your Python script's filename
./101-compile  # Run the shell script

Task 13: ByteCode -> Python #1 (Advanced)
Description: Write a Python function that performs a specific computation as defined in Python bytecode.

Usage:

python
Copy code
from magic_calculation import magic_calculation

result = magic_calculation(a, b)
