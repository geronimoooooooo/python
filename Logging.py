
https://www.demo2s.com/python/python-logging-example.html
https://www.studytonight.com/python/python-logging-in-file
#################################################################
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

>>> logging.info('an info messge')
2017-05-25 00:58:28 INFO     an info messge
#################################################################
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
2020-06-19 11:43:59,887 - This message is to indicate that Admin has just logged in
#################################################################
#importing the module 
import logging 

#now we will Create and configure logger 
logging.basicConfig(format='%(asctime)s - %(levelname)s %(message)s', datefmt='%H:%M:%S') 
# filename="std.log" filemode='a'

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

#some messages to test
logger.debug("This is just a harmless debug message") 
logger.info("This is just an information for you") 
logger.warning("OOPS!!!Its a Warning") 
logger.error("Have you try to divide a number by zero") 
logger.critical("The Internet is not working....")
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
