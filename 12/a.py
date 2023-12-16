class Grid:
    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.width = len(lines[0])
        self.height = len(lines)

    def print(self):
        for line in self.grid:
            print("".join(line))

    def move_up(self, i, j):
        i_new = i
        while i_new > 0:
            if self.grid[i_new - 1][j] in "#O":
                break
            i_new -= 1
        self.grid[i][j] = "."
        self.grid[i_new][j] = "O"

    def tilt_up(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "O":
                    self.move_up(i, j)

    def get_score(self):
        score = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "O":
                    score += self.height - i
        return score


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    grid = Grid(lines)
    grid.tilt_up()

    print(grid.get_score())


if __name__ == "__main__":
    main()
