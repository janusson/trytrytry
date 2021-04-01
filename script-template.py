#!/usr/bin/python
# -*- coding: utf-8 -*-
#   ejanusson_casestudy_vancity.py
#   ⌬ Eric Janusson
#   Python 3.9
'''
Description:
    [short file description]

Returns:
    [type]: [output]
'''

import os
import sys
# import module as mod
# x = mod.function_in_module()

filename = sys.argv[0]

def funk():
    print(filename)
    print(os.getcwd())
    return None

def main():
    funk()

if __name__ == '__main__':
    main()
