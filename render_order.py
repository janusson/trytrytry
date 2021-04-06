#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: set render order
⌬'''

from enum import auto, Enum


class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
