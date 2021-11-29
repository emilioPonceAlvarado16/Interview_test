## Getting Started

## Overview of the solution.

The presented example can be the input and output of this program.

**INPUT**<br />
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00<br />
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br />
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br />
<br />
**OUTPUT:**<br />
ASTRID-RENE: 2<br />
ANDRES-ASTRID: 3<br />
ANDRES-RENE: 2<br />

The input is a file.txt where these logs are saved in plain text.

With this solution, we can get the amount of times where a pair of employees have coincided in the office along the week.

There are implemented the validations for the different kind of inputs, error handlers, and automated tests using the standard library unittest.

## Explanation of the architecture


**main .py** is the main program where invokes all the functions in our customized logModule library.<br />
Inside the **logModule/** directory, there is a file called **functions .py** which contains all the functions of our library. <br />
the **logs/** directory is where all the rvalid records.txt are, and those can be the input for the main.<br />
the **unit_tests/** directory contains the **test_logModule_main.py** file, which is the program for the automated tests.<br />
the **fake_logs/** directory contains all the fake records that will be used for testing purposes.<br />

Inside the file logModule/functions.py we will find:<br />
        1. **find_matches:**  This function recevies two dictionaries that represents the logs of two persons along the week, Returns a tuple of the numbers of matches within the same time range and their names in pair. <br />
        2. **format_validator:** This function will validate if the "day_record" follows the right format.<br />
        3. **is_a_match:** This function will compare two datetime ranges
        and determine if is a match or not.
        Ex1: range1: 10:00-12:00 && range2:11:00-13:00 will return True
        Ex2: range1: 10:00-12:00 && range2:12:02-13:00 will return False<br />
        4. **file_to_records:**  This function will read a file which contains the logs, 
            process it and convert it into a list of dictionaries. <br /> 
        5. **get_results:**  This function receives a list of dictionaries which represents the logs,process it and then return a list of tuples. (pair-names, n_matches).Compare each employee with the others employees and determine the number of matches between them.
        6. **results_to_string:**  This function will convert a list of tuples [(a,b),...] into a single string <br />
        

## Approach and methodology


the function file_to_records, will iterate through the entire file.txt, validating the format for every record using the format_validator, extract the values and save it into a list of dictionaries.

The get_results function will use the generated list of dictionaries from file_to_records function and iterate through the dictionary and check the amount of times where a pair of employees have coincided in the office.
Finally, the results_to_string will convert the results into a string as the output of the program

This program uses the **standard library unittest**, so the approach is that Unit testing makes your code future proof since you anticipate the cases where your code could potentially fail or produce a bug. Though you cannot predict all of the cases, you still address most of them.

The format_validator uses a **regular expression**, which is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.

**Error handling:**  Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).
When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash. So, the approach is when having fake/bad logs, and will raise an error that will help to know how and where the error occurred.

## How to run the program locally.

```bash
python3 main.py
```

## How to run the automated tests.

```bash
cd ./unit_tests
python3 test_logModule_main.py
```



