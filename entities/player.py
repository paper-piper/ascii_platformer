class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = '@'
        self.jump_remaining = 0
        self.max_jump = 3    # number of frames you’ll move up
        self.on_ground = False
