import logging
logging.basicConfig(
    filename='si.log',
    filemode='w',
)
level=logging.DEBUG
logging.debug("this is a debug message")
logging.info("this is the info")
logging.error("this is the error")