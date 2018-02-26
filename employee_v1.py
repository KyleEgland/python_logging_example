#! python3
# Python 3 logging example
# The original code for this project came from Corey Schafer on Youtube
# https://youtu.be/-ARI4Cz-awo <- Basic logging video
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:
    # A sample Employee class

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        logging.info('Created Employee: {} - {}\
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
