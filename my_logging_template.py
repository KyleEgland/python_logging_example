#! python3
# This is the logging template that I copy/paste into my projects
import logging
import os
import sys


# ------------ #
# Logger Setup #
# ------------ #
# Check for the existence of a 'logs' folder - should one not exist, create it
if os.path.exists('./logs/'):
    pass
else:
    try:
        os.mkdir('./logs/')
    except Exception as e:
        print('[-] Unable to create directory - please check permissions')
        sys.exit()
#
# LOGGER creation
logger = logging.getLogger(__name__)
#
# LOGGER set level: Debug -> Info -> Warning -> Error -> Critical
logger.setLevel(logging.DEBUG)
#
# FORMATTER creation
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                              datefmt='%d-%b-%Y %H')
#
# FILE HANDLER creation
file_handler = logging.FileHandler('./logs/{}.log'.format(__name__))
#
# FILE HANDLER set formatter
file_handler.setFormatter(formatter)
#
# FILE HANDLER set level
file_handler.setLevel(logging.ERROR)
#
# STREAM HANDLER creation
stream_handler = logging.StreamHandler()
# STREAM HANDLER set formatter
stream_handler.setFormatter(formatter)
#
# LOGGER add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# NOTES:
# use logger.exception() to get the traceback in addtion to log message
# ---------------------- #
# ----- End Logger ----- #
# ---------------------- #


if __name__ == "__main__":
    # Test the logger as-is in this file
    # All messages should show up in console (given above config)
    logger.debug('This is a DEBUG message.')
    logger.info('This is an INFO messaage')
    logger.warning('This is a WARNING message')
    # Only these messages should show up in the log file (give above config)
    logger.error('This is an ERROR message')
    logger.critical('This is a CRITICAL message')
