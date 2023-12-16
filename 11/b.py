class Grid:
    def __init__(self, lines, expansion_factor=1):
        self.grid = [list(line.strip()) for line in lines]
        self.width, self.height = len(self.grid[0]), len(self.grid)
        self.expansion_factor = expansion_factor

        self.expansion_rows = []
        self.expansion_cols = []
        self.expand()

        self.galaxies = None
        self.get_galaxy_coordinates()

    def expand(self):
        rows_to_add, cols_to_add = [], []
        for r in range(self.height):
            if all(self.grid[r][c] == "." for c in range(self.width)):
                self.expansion_rows.append(r)
        for c in range(self.width):
            if all(self.grid[r][c] == "." for r in range(self.height)):
                self.expansion_cols.append(c)

    def get_galaxy_coordinates(self):
        self.galaxies = []

        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == "#":
                    self.galaxies.append((r, c))

    def get_distance(self, g1, g2):
        r1, c1 = g1
        r2, c2 = g2

        distance = abs(r1 - r2) + abs(c1 - c2)
        for r in self.expansion_rows:
            if min(r1, r2) < r < max(r1, r2):
                distance += self.expansion_factor - 1
        for c in self.expansion_cols:
            if min(c1, c2) < c < max(c1, c2):
                distance += self.expansion_factor - 1

        return distance

    def get_shortest_path_sum(self):
        ans = 0
        for i, g1 in enumerate(self.galaxies):
            for g2 in self.galaxies[i + 1 :]:
                ans += self.get_distance(g1, g2)
        return ans

    def print(self):
        print("Galaxy map")
        for r in self.grid:
            print("".join(r))


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    grid = Grid(lines, expansion_factor=1000000)

    ans = grid.get_shortest_path_sum()
    print(ans)


if __name__ == "__main__":
    main()
