import logging
import time,sys
from logging.handlers import TimedRotatingFileHandler


log = logging.getLogger('yyx')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

log_file_handler = TimedRotatingFileHandler(filename="/home/shenhao/tool/pypro/basepy/agent", when="S", interval=2)
log_file_handler.setFormatter(formatter)
log_file_handler.setLevel(logging.DEBUG)
log.addHandler(log_file_handler)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
