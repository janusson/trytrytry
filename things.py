class Entity:
    '''
    Factory for generic entities like players, items, etc.
    '''
    def __init__(self, x, y, character, colour):
        self.x = x
        self.y = y
        self.char = character
        self.color = colour

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        