class Card:
    def __init__(self, string):
        label, rest = string.split(": ")

        self.id = int(label.split()[1])

        self.winning = set(map(int, rest.split(" | ")[0].split()))
        self.numbers = list(map(int, rest.split(" | ")[1].split()))

    def get_score(self):
        return len([x for x in self.numbers if x in self.winning])


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    cards = [Card(line) for line in lines]
    counts = {n: 1 for n in range(len(cards))}

    for i, c in enumerate(cards):
        score = c.get_score()
        for j in range(i + 1, min(i + score + 1, len(cards))):
            counts[j] += counts[i]

    print(sum(counts.values()))


if __name__ == "__main__":
    main()
