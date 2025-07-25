import curses


class InputHandler:
    def __init__(self, screen):
        self.screen = screen

    def get_action(self):
        key = self.screen.getch()
        if key in (ord('a'), curses.KEY_LEFT):
            return 'left'
        if key in (ord('d'), curses.KEY_RIGHT):
            return 'right'
        if key in (ord('w'), curses.KEY_UP, ord(' ')):
            return 'jump'
        if key in (ord('q'), ord('Q')):
            return 'quit'
        return None
