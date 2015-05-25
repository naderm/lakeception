# -*- coding: utf-8 -*-
import pygame
import sys
import os

from world import World
from screen import Screen
from input import Input

class Game(object):
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) # setup mixer to avoid sound lag
        pygame.init()
        pygame.display.set_caption("lakeception")
        
        self.world = World("Test World", (100,100), debug=False)
                                       # resolution, viewport
        self.screen = Screen(self.world, (800, 475), (25, 11))
        self.input = Input(self)
        
        self.fps = 60
        self.clock = pygame.time.Clock()
        
        self.ANIMATE = pygame.USEREVENT+0
        self.animation_rate = 1 * 1000
        # Temporarily (?) disabled animations, because moving + animating was
        # an INTENSE visual experience
        # pygame.time.set_timer(self.ANIMATE, self.animation_rate)
        
        self.updated = True
        self.quitting = False
        self.muted = False

        pygame.mixer.init()
        # From https://www.freesound.org/people/juskiddink/sounds/60507/
        # albeit a bit mixed to allow for looping
        pygame.mixer.music.load(os.path.join(sys.path[0], '60507__juskiddink__waves2.ogg'))
        pygame.mixer.music.play(-1)
        # Set the volume to an unobtrusive level
        pygame.mixer.music.set_volume(0.1)
 
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.input.handleKey(event)
            elif event.type == self.ANIMATE:
                self.screen.draw()
                self.updated = False
            elif event.type == pygame.QUIT:
                self.quitting = True
        
        if self.updated:
            self.screen.draw()
            self.updated = False
        
        timeDelta = self.clock.tick(self.fps)

if __name__ == "__main__":
    g = Game()
    while not g.quitting:
        g.tick()
