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

# Log levels (low-high): Debug -> Info -> Warning -> Error -> Critical
# Instantiate a logger - instead of using root - to allow files to log
# independently (if there are multiple files in a project)
logger = logging.getLogger(__name__)

# This establishes what level to log (ref. log levels above)
logger.setLevel(logging.DEBUG)

# Format the string that prepends the information that goes into the log file
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                              datefmt='%d-%b-%Y %H')

# Create/name the log file
file_handler = logging.FileHandler('./logs/{}.log'.format(__name__))

# Link the specified format above to the logger
file_handler.setFormatter(formatter)

# Capture only Errors and above in file handler - this overrides ".setLevel"
# for the file
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
# NOTES:
# use logger.exception() to get the traceback in addtion to log message

# ---------- #
# End Logger #
# ---------- #


if __name__ == "__main__":
    # Test the logger as-is in this file
    # All messages should show up in console (given above config)
    logger.debug('This is a DEBUG message.')
    logger.info('This is an INFO messaage')
    logger.warning('This is a WARNING message')
    # Only these messages should show up in the log file (give above config)
    logger.error('This is an ERROR message')
    logger.critical('This is a CRITICAL message')
