MOVES = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}


class Grid:
    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.width = len(lines[0])
        self.height = len(lines)

    def print(self):
        for line in self.grid:
            print("".join(line))

    def move(self, i, j, direction):
        i_new = i
        j_new = j

        while (
            0 <= i_new + direction[0] < self.height
            and 0 <= j_new + direction[1] < self.width
        ):
            if self.grid[i_new + direction[0]][j_new + direction[1]] in "#O":
                break
            i_new += direction[0]
            j_new += direction[1]
        self.grid[i][j] = "."
        self.grid[i_new][j_new] = "O"

    def tilt(self, direction):
        ivals = (
            range(self.height) if direction[0] == -1 else range(self.height - 1, -1, -1)
        )
        jvals = (
            range(self.width) if direction[1] == -1 else range(self.width - 1, -1, -1)
        )

        for i in ivals:
            for j in jvals:
                if self.grid[i][j] == "O":
                    self.move(i, j, direction)

    def get_score(self):
        score = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "O":
                    score += self.height - i
        return score

    def cycle(self):
        self.tilt(MOVES["UP"])
        self.tilt(MOVES["LEFT"])
        self.tilt(MOVES["DOWN"])
        self.tilt(MOVES["RIGHT"])

    def __str__(self):
        string = ["".join(line) for line in self.grid]
        return "".join(string)

    @classmethod
    def from_string(cls, string, width, height):
        lines = [string[i * width : (i + 1) * width] for i in range(height)]
        return cls(lines)


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    NUM_CYCLES = 1000000000

    grid = Grid(lines)
    width, height = grid.width, grid.height

    state_to_index = {}
    index_to_state = {}

    for i in range(1, NUM_CYCLES + 1):
        grid.cycle()
        if str(grid) in state_to_index:
            cycle_start = state_to_index[str(grid)]
            cycle_length = i - cycle_start
            break

        state_to_index[str(grid)] = i
        index_to_state[i] = str(grid)

    target_index = (NUM_CYCLES - cycle_start) % cycle_length + cycle_start
    grid = Grid.from_string(index_to_state[target_index], width, height)
    print(grid.get_score())


if __name__ == "__main__":
    main()
