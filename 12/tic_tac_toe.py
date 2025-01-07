class TTT:
    def __init__(self):
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    
    def check(self):
        indexes = tuple(range(3))
        for row in indexes:
            all_values = [
                [self.grid[row][column] for column in indexes],
                [self.grid[column][row] for column in indexes],
                [self.grid[column][column] for column in indexes],
                # chybí zpětná diagonála # ignore this
            ]

            for values in all_values:
                result = sum(values)
                if abs(result) == 3:
                    return result


    def set(self, x, y, value):
        self.grid[x][y] = value
    
    def set_x(self, x, y):
        self.set(x, y, 1)

    def set_o(self, x, y):
        self.set(x, y, -1)

    def render(self):
        keys = {1: 'x', -1: 'o', 0: ' '}
        data = [' | '.join(keys[value] for value in row) for row in self.grid]
        data = '\n---------\n'.join(data)
        print(data)



t = TTT()
t.set_o(0, 0)
t.set_o(1, 0)
t.set_o(2, 0)
t.render()
print(t.check())