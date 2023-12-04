class Card:
    def __init__(self, string):
        label, rest = string.split(": ")

        self.id = int(label.split()[1])

        self.winning = set(map(int, rest.split(" | ")[0].split()))
        self.numbers = list(map(int, rest.split(" | ")[1].split()))

    def get_score(self):
        count = len([x for x in self.numbers if x in self.winning])
        score = 2 ** (count - 1) if count > 0 else 0
        return score


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        card = Card(line)
        total += card.get_score()

    print(total)


if __name__ == "__main__":
    main()
