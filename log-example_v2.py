#! python3
# Python 3 logging example
# The original code for this project came from Corey Schafer on Youtube
# https://youtu.be/jxmzY9soFXg <- Advanced logging video
# Logging is built into Python
import logging
# Importing the employee script - code will run on import which causes this
# scripts logger not to run if everything is left as-is from v1 scripts.  This
# is because each script is "sharing" the "root logger"
import employee_v2

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

# Setting up this file to also run its own logger - instead of using root
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(formatter)
# Capture only Errors and above in file handler
file_handler.setLevel(logging.ERROR)

# Adding stream handler to put debug statements in console
stream_handler = logging.StreamHandler()
# Don't need to set logging level on this because the logger itself is
# set to DEBUG already
# Set formatting of stream handler to be the same as the log file
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# Add stream handler to the logger
logger.addHandler(stream_handler)

# Changing logging module basic configurations:
# Log file, log level, and changing format of log
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

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
    try:
        result = x / y
    except ZeroDivisionError:
        # This statement will log the traceback
        logger.exception('Tried to divide by zero')
    else:
        return result


# Variables
num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
