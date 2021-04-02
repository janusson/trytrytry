import logging
# deault log setup
log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

def debug_logger():
    '''
    Sets up a simple debug logger for development.
    '''
    file_handler = logging.FileHandler(f'./log/{__name__}.log')
    logger.setLevel(logging.DEBUG)
    return debug_logger

def logfile_record():
    file_handler = logging.FileHandler(f'./log/{__name__}.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)
    return file_handler

def stream_handler():
    streamer = logging.StreamHandler()
    streamer.setLevel(logging.INFO)
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(streamer)

# TODO finish setting up logging with choice of stream handler. 
# export logfiles to 'log' output folder
# see debugging, corey schafer on youtube, for more details

if __name__ == "__main__":
    debug_logger()
    logfile_record()
    # stream_handler()
    print('Debug logging initialized.')