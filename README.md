## Getting Started

## Overview of the solution

Let's show an example of the input and output of this program

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
ASTRID-RENE: 2
ANDRES-ASTRID: 3
ANDRES-RENE: 2

The input is a file.txt where these logs are saved in plain text.

With this solution, we can get the amount of times where a pair of employees have coincided in the office along the week.

There are the necessary validations for the different kind of inputs, error handlers, and automated tests using the standard library unittest.


## How to run the program locally.

```bash
python3 main.py
```

## How to run the automated tests.

```bash
cd ./unit_tests
python3 test_logModule_main.py
```



