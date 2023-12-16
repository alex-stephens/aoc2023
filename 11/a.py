class Grid:
    def __init__(self, lines):
        self.grid = [list(line.strip()) for line in lines]
        self.width, self.height = len(self.grid[0]), len(self.grid)

        self.expand()

        self.galaxies = None
        self.get_galaxy_coordinates()

    def expand(self):
        rows_to_add, cols_to_add = [], []
        for r in range(self.height):
            if all(self.grid[r][c] == "." for c in range(self.width)):
                rows_to_add.append(r)
        for c in range(self.width):
            if all(self.grid[r][c] == "." for r in range(self.height)):
                cols_to_add.append(c)

        for r in rows_to_add[::-1]:
            self.grid.insert(r, ["."] * self.width)
        self.height += len(rows_to_add)

        for c in cols_to_add[::-1]:
            for r in range(self.height):
                self.grid[r].insert(c, ".")
        self.width += len(cols_to_add)

    def get_galaxy_coordinates(self):
        self.galaxies = []

        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == "#":
                    self.galaxies.append((r, c))

    def get_shortest_path_sum(self):
        ans = 0
        for i, g1 in enumerate(self.galaxies):
            for j, g2 in enumerate(self.galaxies[i + 1 :]):
                r1, c1 = g1
                r2, c2 = g2

                ans += abs(r1 - r2) + abs(c1 - c2)

        return ans

    def print(self):
        print("Galaxy map")
        for r in self.grid:
            print("".join(r))


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    grid = Grid(lines)

    ans = grid.get_shortest_path_sum()
    print(ans)


if __name__ == "__main__":
    main()
