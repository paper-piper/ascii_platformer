class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def render(self, level):
        max_y, max_x = self.screen.getmaxyx()
        offset_y = max((max_y - level.height) // 2, 1)
        offset_x = max((max_x - level.width) // 2, 1)

        for y, line in enumerate(level.map_data):
            display_line = line.ljust(level.width)
            if offset_y + y < max_y - 1:
                self.screen.addstr(offset_y + y, offset_x, display_line[:level.width])
        return offset_y, offset_x
