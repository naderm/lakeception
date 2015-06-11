# -*- coding: utf-8 -*-
import random

from lakeutils import hex2rgb

# Nice Tile Graveyard (nice tiles you found but don't know what to do with)
# Tile("?", "a mysterious secret", "0", "333333")
# Tile("unknown", "something unknown", "!", "B65555")

class Tile(object):
    def __init__(self, name, description, icons, color, collidable=False):
        self.name = name
        self.collidable = collidable
        self.description = description
        # A collection of characters representing the tile.
        # A random icon is chosen each frame draw for ~ambience~
        self.icon = random.choice(icons)
        self.color = hex2rgb(color)
    
    def __unicode__(self):
        return self.icon
    
    def __repr__(self):
        return self.__unicode__()

    def __hash__(self):
        return hash((self.icon, self.color))

    def __eq__(self, other):
        return (self.icon, self.color) == (other.icon, other.color)

