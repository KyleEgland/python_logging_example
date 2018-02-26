#! python3
# Python 3 logging example
# The original code for this project came from Corey Schafer on Youtube
# https://youtu.be/jxmzY9soFXg <- Advanced logging video
import logging

# Creating logger variable - convention is to use __name__ variable.  This
# means that when the logger is launched via the script it's in, the name will
# be "main".  If the logger is launched via a script that is imported, it's
# name will be the name of the script (I.e. employee_v2).
logger = logging.getLogger(__name__)
# After creating the new logger variable, it needs to be used.  The log
# statement below is therefore changed from logging to logger.
# Set log level
logger.setLevel(logging.INFO)

# Creating a formatter to handle the formatting of the output to the log file
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# Need to add a file handler for the new logger - allows the specification of
# the file to be logged to
file_handler = logging.FileHandler('employee.log')
# Adding the formatter to the file handler
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# Setting the basic config in this maner is only for the "root" logger - left
# here as an example.
# logging.basicConfig(filename='employee.log', level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:
    # A sample Employee class

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}\
                     '.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Kyle', 'Johnson')
emp_3 = Employee('Jane', 'Doe')
