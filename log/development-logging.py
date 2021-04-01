import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

def file_logger():
    file_handler = logging.FileHandler(f'./log/{__name__}.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

def stream_handler():
    streamer = logging.StreamHandler()
    streamer.setLevel(logging.INFO)
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(streamer)

# start = (datetime.today()).timestamp() # Keep track of rotation time
