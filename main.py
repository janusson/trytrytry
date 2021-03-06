#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: Handles entities like player, monsters, etc.
⌬'''
import copy
import tcod
from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 60

    map_width = 75
    map_height = 50

    room_max_size = 10
    room_min_size = 8
    max_rooms = 15

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="trytrytry",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            engine.event_handler.handle_events()


if __name__ == "__main__":
    main()
