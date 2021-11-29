## Getting Started

## Overview of the solution.

The presented example can be the input and output of this program.

INPUT<br />
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00<br />
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br />
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br />
<br />
OUTPUT:<br />
ASTRID-RENE: 2<br />
ANDRES-ASTRID: 3<br />
ANDRES-RENE: 2<br />

The input is a file.txt where these logs are saved in plain text.

With this solution, we can get the amount of times where a pair of employees have coincided in the office along the week.

There are implemented the validations for the different kind of inputs, error handlers, and automated tests using the standard library unittest.

## Explanation of the architecture


main.py is the main program where invokes all the functions in our customized logModule library.<br />
the logModule/ directory is where all the functions are. <br />
the logs/ directory is where all the records.txt are, and those can be the input for the main.<br />
the unit_tests/ directory contains the test_logModule_main.py, which is the program for the automated tests.<br />
the fake_logs/ directory contains all the fake records that will be used for testing purposes.<br />

Inside the file logModule/functions.py we will find:<br />
        1. find_matches <br />
        2. format_validator<br />
        3. is_a_match<br />
        4. file_to_records<br />
        5. get_results<br />
        6. results_to_string<br />

## Approach and methodology


## How to run the program locally.

```bash
python3 main.py
```

## How to run the automated tests.

```bash
cd ./unit_tests
python3 test_logModule_main.py
```



