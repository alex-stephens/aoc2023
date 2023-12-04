class Schematic:
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append([c for c in line])

        # Each number has (value, start-coord, end-coord)
        self.numbers = []
        self.find_numbers()

        self.symbols = []
        self.find_symbols()

    def find_numbers(self):
        num_str = None

        for i, row in enumerate(self.grid):
            for j, c in enumerate(row):
                # Start of a number
                if c.isdigit() and (j == 0 or not (row[j - 1]).isdigit()):
                    num_str = c

                elif c.isdigit():
                    num_str += c

                # End of a number
                if (not c.isdigit() and num_str is not None) or (
                    j == len(row) - 1 and c.isdigit()
                ):
                    self.numbers.append(
                        (int(num_str), (i, j - len(num_str)), (i, j - 1))
                    )
                    num_str = None

    def find_symbols(self):
        for i, row in enumerate(self.grid):
            for j, c in enumerate(row):
                if not c.isdigit() and c != ".":
                    self.symbols.append((c, (i, j)))

    def is_near_symbol(self, number):
        for symbol in self.symbols:
            if self.is_near(number, symbol):
                return True

        return False

    def is_near(self, number, symbol):
        i = number[1][0]
        for j in range(number[1][1], number[2][1] + 1):
            if abs(i - symbol[1][0]) <= 1 and abs(j - symbol[1][1]) <= 1:
                return True
        return False

    def get_part_numbers(self):
        part_numbers = []
        for n in self.numbers:
            if self.is_near_symbol(n):
                part_numbers.append(n[0])
                continue
        return part_numbers

    def get_nearby_numbers(self, symbol):
        nearby = []
        for number in self.numbers:
            if self.is_near(number, symbol):
                nearby.append(number)
        return nearby

    def get_gear_ratio_sum(self):
        ans = 0
        for symbol in self.symbols:
            nearby = self.get_nearby_numbers(symbol)
            if len(nearby) == 2:
                ans += nearby[0][0] * nearby[1][0]

        return ans


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    s = Schematic(lines)

    ans = s.get_gear_ratio_sum()
    print(ans)


if __name__ == "__main__":
    main()
