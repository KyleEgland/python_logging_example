#! python3
# Python 3 logging example
# The original code for this project came from Corey Schafer on Youtube
# https://youtu.be/-ARI4Cz-awo
# Logging is built into Python
import logging

# Logging levels:
# DEBUG:  Detailed information, typically of interest only when diagnosing
#         problems.
# INFO:  Confirmation that things are working as expected.
# WARNING:  An indication that something unexpected happened, or indicative of
#           some problem in the near future (e.g. 'disk space low').  The
#           software is still working as expected
# Error:  Due to a more serious problem, the software has not been able to
#         perform some function
# CRITICAL:  A serious error, indicating that the program itself may be unable
#            to continue running.
# Default log leve is warning (covering warning - critical).  The default
# action of the logging module is to log to console

# Changing logging module basic configurations:
# Log file, log level, and changing format of log
# https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Changing format of log
# https://docs.python.org/3/library/logging.html#logrecord-attributes


def add(x, y):
    # Add function
    return x + y


def subtract(x, y):
    # Subtract function
    return x - y


def multiply(x, y):
    # Multiply Function
    return x * y


def divide(x, y):
    # Divide function
    return x / y


# Variables
num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
