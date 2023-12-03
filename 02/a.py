COLOURS = set(["red", "green", "blue"])


class Game:
    def __init__(self, string):

        s1, s2 = string.split(": ")
        self.id = int(s1.split(" ")[1])

        print(self.id)
        self.draws = []
        for draw in s2.split("; "):
            self.draws.append({})
            for c in draw.split(", "):
                num, colour = c.split(" ")
                num = int(num)
                self.draws[-1][colour] = num
        print(self.draws)

    def is_possible(self, query):
        for draw in self.draws:
            for colour in draw:
                if draw[colour] > query[colour]:
                    return False
        return True


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    games = [Game(line) for line in lines]
    ans = 0

    query = {"red": 12, "green": 13, "blue": 14}

    for game in games:
        if game.is_possible(query):
            ans += game.id
    print(ans)


if __name__ == "__main__":
    main()
