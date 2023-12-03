from numpy import prod

COLOURS = set(["red", "green", "blue"])


class Game:
    def __init__(self, string):

        s1, s2 = string.split(": ")
        self.id = int(s1.split(" ")[1])

        self.draws = []
        for draw in s2.split("; "):
            self.draws.append({})
            for c in draw.split(", "):
                num, colour = c.split(" ")
                num = int(num)
                self.draws[-1][colour] = num

    def is_possible(self, query):
        for draw in self.draws:
            for colour in draw:
                if draw[colour] > query[colour]:
                    return False
        return True

    def compute_min_power(self):

        min_set = {c: 0 for c in COLOURS}

        for draw in self.draws:
            for colour in draw:
                min_set[colour] = max(min_set[colour], draw[colour])

        return prod(list(min_set.values()))


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    games = [Game(line) for line in lines]
    ans = 0

    for game in games:
        power = game.compute_min_power()
        ans += power

    print(ans)


if __name__ == "__main__":
    main()
