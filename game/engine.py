import curses
import os
import time

from world.level import Level
from render.renderer import Renderer
from entities.player import Player
from game.input_handler import InputHandler


class GameEngine:
    def __init__(self):
        level_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'levels', 'level1.txt')
        self.level = Level.load_from_file(level_path)
        spawn_x, spawn_y = self.level.find_spawn()
        self.player = Player(spawn_x, spawn_y)

    def run(self):
        curses.wrapper(self._main)

    def _main(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.keypad(True)
        self.input_handler = InputHandler(stdscr)
        renderer = Renderer(stdscr)

        while True:
            action = self.input_handler.get_action()
            if action == 'quit':
                break

            if action in ('left', 'right'):
                dx = -1 if action == 'left' else 1
                new_x = self.player.x + dx
                if 0 <= new_x < self.level.width and self.level.map_data[self.player.y][new_x] != '#':
                    self.player.x = new_x

            # initiate jump if on ground
            if action == 'jump' and self.player.on_ground:
                self.player.jump_remaining = self.player.max_jump
                self.player.on_ground = False

            # apply vertical movement: jump arc then gravity
            if self.player.jump_remaining > 0:
                # try moving up one cell
                new_y = self.player.y - 1
                if new_y >= 0 and self.level.map_data[new_y][self.player.x] not in ('#', '='):
                    self.player.y = new_y
                else:
                    # hit ceiling, cancel remaining jump
                    self.player.jump_remaining = 0
                self.player.jump_remaining -= 1
            else:
                # gravity: fall unless standing on floor or platform
                below = self.player.y + 1
                if below < self.level.height and self.level.map_data[below][self.player.x] not in ('#', '='):
                    self.player.y = below
                    self.player.on_ground = False
                else:
                    self.player.on_ground = True

            stdscr.clear()
            stdscr.border()
            offset_y, offset_x = renderer.render(self.level)
            stdscr.addch(offset_y + self.player.y, offset_x + self.player.x, self.player.symbol)
            stdscr.refresh()
            time.sleep(1/30)
