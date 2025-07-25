import curses
import os

from world.level import Level
from render.renderer import Renderer


class GameEngine:
    def __init__(self):
        # Load the first level from the assets folder
        level_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'levels', 'level1.txt')
        self.level = Level.load_from_file(level_path)

    def run(self):
        curses.wrapper(self._main)

    def _main(self, stdscr):
        # Configure curses
        curses.curs_set(0)         # Hide cursor
        stdscr.nodelay(False)      # Blocking input
        stdscr.clear()

        # Draw border around entire terminal window
        stdscr.border()

        # Render the static level map inside the border
        renderer = Renderer(stdscr)
        renderer.render(self.level)
        stdscr.refresh()

        # Wait for a key press before exiting
        stdscr.getch()
