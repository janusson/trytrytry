#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Eric Janusson
#   Python 3.9
'''⌬
Description: Basic game components.
⌬'''

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class BaseComponent:
    entity: Entity  # Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine
