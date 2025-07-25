class Level:
    def __init__(self, map_data):
        # map_data is a list of 20 strings, each 60 chars long
        self.map_data = map_data

    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as f:
            lines = [f.readline().rstrip('\n').replace('.', ' ') for _ in range(20)]
        return Level(lines)
