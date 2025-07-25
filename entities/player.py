from world.level import Level

class Player:
    # Physics tuning: slower gravity and fall speed for smoother movement
    GRAVITY = 0.15           # gravity acceleration per tick (slowed further)
    JUMP_STRENGTH = -1.0     # initial upward velocity (gentler jump)
    MAX_FALL_SPEED = 1.5     # terminal velocity (slower fall)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # Use a float for sub-tile vertical movement
        self.y_float = float(y)
        self.symbol = '@'
        self.vx = 0             # horizontal velocity
        self.vy = 0.0           # vertical velocity
        self.on_ground = False  # is the player standing on solid ground?
        self.SOLID_TILES = {'#', '='}

    def move(self, dx: int, dy: int, level: Level):
        # Handle horizontal movement
        if dx != 0:
            target_x = self.x + dx
            if 0 <= target_x < level.width:
                if level.map_data[self.y][target_x] not in self.SOLID_TILES:
                    self.x = target_x

        # Handle vertical movement in integer steps for collisions
        if dy != 0:
            step = 1 if dy > 0 else -1
            for _ in range(abs(dy)):
                target_y = self.y + step
                if 0 <= target_y < level.height:
                    if level.map_data[target_y][self.x] in self.SOLID_TILES:
                        # Collision: stop vertical movement
                        self.vy = 0
                        self.on_ground = (step > 0)
                        break
                    else:
                        self.y = target_y
                        self.y_float = float(self.y)
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
        # Apply gravity acceleration, clamped by terminal velocity
        self.vy = min(self.vy + self.GRAVITY, self.MAX_FALL_SPEED)
        # Update floating position, then convert to integer movement
        self.y_float += self.vy

        dy = int(self.y_float) - self.y
        if dy != 0:
            self.move(0, dy, level)

    def update(self, keys: set, level: Level):
        # Reset horizontal velocity
        self.vx = 0
        # Process movement inputs
        if 'left' in keys and 'right' not in keys:
            self.move_left(level)
        elif 'right' in keys and 'left' not in keys:
            self.move_right(level)
        # Process jump input
        if 'jump' in keys:
            self.jump()
        # Apply gravity and vertical motion
        self.apply_gravity(level)
