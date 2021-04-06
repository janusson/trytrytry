#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: set render order
⌬'''

import time
import logging

# constants
start_time = time.time()

# logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(f'./log/{__name__}.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
file_handler.setLevel(logging.INFO)
stream_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
