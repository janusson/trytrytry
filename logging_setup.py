# Start Here:

import os
import sys
import subprocess
import time
import logging

# constants
start_time = time.time()
# default location of Driftscope Apex3D64.exe and logfile
apexPath = r'C:\DriftScope\lib\Apex3D64.exe'
apexLogPath = r'C:\DriftScope\log\_Apex3DLog.txt'

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
