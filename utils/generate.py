import noise

class init:
    def __init__(self, size: tuple, seed):
        self.world = [[0 for _ in range(size[0])] for _ in range(size[1])]

        for x in range(size[0]):
            for y in range(size[1]):

                n = noise.pnoise2((x / 100) + 10, (y / 100), octaves=6, base=seed)
                
                if abs(n) > 0.15:   # Darker dirt
                    self.world[y][x] = 3
                elif abs(n) > 0.04: # Dirt
                    self.world[y][x] = 1
                elif abs(n) > 0.02: # Water
                    self.world[y][x] = 2

    def getArr(self):
        return self.world
