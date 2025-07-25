class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def render(self, level):
        """
        Draw the level map centered on the screen.
        Assumes a fixed level size of 60x20 characters.
        """
        max_y, max_x = self.screen.getmaxyx()
        level_height = 20
        level_width = 60

        start_y = (max_y - level_height) // 2
        start_x = (max_x - level_width) // 2

        for y, line in enumerate(level.map_data):
            display_line = line.ljust(level_width)
            self.screen.addstr(start_y + y, start_x, display_line)