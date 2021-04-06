#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: trytrytry
⌬'''

import libtcodpy as libtcod
from input_handlers import handle_keys
from things import Entity
import render_functions as rf

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width /2 -5), int(screen_height /2), '@', libtcod.yellow)
    entities = [player, npc]

    libtcod.console_set_custom_font('./images/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'trytrytry', False)

    console = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        # libtcod.console_set_default_foreground(console, libtcod.white)
        # libtcod.console_put_char(console, player.x, player.y, '@', libtcod.BKGND_NONE)
        # libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)
        rf.render_all(console, entities, screen_width, screen_height)
        libtcod.console_flush()

        libtcod.console_put_char(console, player.x, player.y, ' ', libtcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
     main()
