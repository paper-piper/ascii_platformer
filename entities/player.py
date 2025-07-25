from world.level import Level

class Player:
    GRAVITY = 1            # gravity acceleration per tick
    JUMP_STRENGTH = -3     # initial upward velocity
    MAX_FALL_SPEED = 3     # terminal velocity
    SOLID_TILES = {'#', '='}

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.symbol = '@'
        self.vx = 0     # horizontal velocity
        self.vy = 0     # vertical velocity
        self.on_ground = False

    def move(self, dx: int, dy: int, level: Level):
        # Horizontal movement
        if dx != 0:
            target_x = self.x + dx
            if 0 <= target_x < level.width:
                if level.map_data[self.y][target_x] not in self.SOLID_TILES:
                    self.x = target_x
        # Vertical movement (handles multiple-step fall/jump)
        if dy != 0:
            step = 1 if dy > 0 else -1
            for _ in range(abs(dy)):
                target_y = self.y + step
                if 0 <= target_y < level.height:
                    if level.map_data[target_y][self.x] in self.SOLID_TILES:
                        # collision with floor/ceiling
                        self.vy = 0
                        self.on_ground = (step > 0)
                        break
                    else:
                        self.y = target_y
                else:
                    break

    def move_left(self, level: Level):
        self.vx = -1
        self.move(self.vx, 0, level)

    def move_right(self, level: Level):
        self.vx = 1
        self.move(self.vx, 0, level)

    def jump(self):
        if self.on_ground:
            self.vy = self.JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self, level: Level):
        # accelerate downward
        self.vy = min(self.vy + self.GRAVITY, self.MAX_FALL_SPEED)
        self.move(0, self.vy, level)

    def update(self, keys: set, level: Level):
        # Reset horizontal velocity each tick
        self.vx = 0
        # Process inputs
        if 'left' in keys and 'right' not in keys:
            self.move_left(level)
        elif 'right' in keys and 'left' not in keys:
            self.move_right(level)
        # Jump if requested
        if 'jump' in keys:
            self.jump()
        # Apply physics
        self.apply_gravity(level)