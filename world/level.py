class Level:
    def __init__(self, map_data):
        self.map_data = map_data
        self.height = len(map_data)
        self.width = len(map_data[0]) if self.height else 0

    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as f:
            lines = [f.readline().rstrip('\n').replace('.', ' ') for _ in range(20)]
        return Level(lines)

    def find_spawn(self):
        for y, row in enumerate(self.map_data):
            if '@' in row:
                x = row.index('@')
                row_list = list(self.map_data[y])
                row_list[x] = ' '
                self.map_data[y] = ''.join(row_list)
                return x, y
        return 0, 0
