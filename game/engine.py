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
        renderer = Renderer(stdscr)
        self.input_handler = InputHandler()

        while True:
            actions = self.input_handler.get_actions()
            if 'quit' in actions:
                break

            self.player.update(actions, self.level)

            stdscr.clear()
            stdscr.border()
            offset_y, offset_x = renderer.render(self.level)
            stdscr.addch(offset_y + self.player.y, offset_x + self.player.x, self.player.symbol)
            stdscr.refresh()
            time.sleep(1 / 30)

