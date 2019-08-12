import logging

class Log:
    def __init__(self,msg):
        self.msg = msg
    
    def info(self):
        FORMAT  = "%(asctime)-15s%(message)s"
        logging.basicConfig(filemode = "w", filename="debug.log", format = FORMAT, level=logging.INFO)
        logging.info(self.msg)
    
    def error(self):
        FORMAT  = "%(asctime)-15s%(message)s"
        logging.basicConfig(filemode = "w", filename="debug.log", format = FORMAT, level=logging.ERROR)
        logging.error(self.msg)