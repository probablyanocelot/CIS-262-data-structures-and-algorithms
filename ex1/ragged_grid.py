import random

class RaggedGrid:
    def __init__(self, grid):
        self.grid = grid

    def populate_random(self, max_value=100):
        unique_numbers = random.sample(range(1, max_value + 1), sum(len(row) for row in self.grid))
        index = 0
        for row in self.grid:
            for i in range(len(row)):
                row[i] = unique_numbers[index]
                index += 1

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        return max(len(row) for row in self.grid)

# Example usage
ragged_grid = RaggedGrid([[0] * 3, [0] * 6, [0] * 9])
print(ragged_grid.grid)
ragged_grid.populate_random()
print(ragged_grid.grid)
print("Height:", ragged_grid.get_height())
print("Width:", ragged_grid.get_width())