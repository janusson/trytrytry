#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: Handles entities like player, monsters, etc.
⌬'''

from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char='@',
    color=(255, 255, 255),
    name='The Wizard',
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

smelly_gobbo = Actor(
    char='O',
    color=(80, 150, 50),
    name='Smelly Gobbo',
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3)
    )
