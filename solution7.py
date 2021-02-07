'''
Write a script which can read the files line by line with .log ext and print it into a
file , while printing the data from the suffix with present date and time of the system.

'''


import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create a file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create a console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# now add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
