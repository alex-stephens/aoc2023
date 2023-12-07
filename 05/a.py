class Map:
    def __init__(self, block):
        title = block[0][:-5].split("-")

        self.source = title[0]
        self.dest = title[-1]

        self.ranges = [list(map(int, r.split())) for r in block[1:]]
        self.mapping = {}

    def convert(self, value):
        for dest, source, range_ in self.ranges:
            if source <= value <= source + range_ - 1:
                return dest + value - source

        return value


def main():
    filename = "input.txt"

    with open(filename) as f:
        seeds = list(map(int, f.readline().split(": ")[1].split()))

        lines = [line.strip() for line in f.readlines()]

    blocks = []
    for line in lines:
        if line == "":
            blocks.append([])
        else:
            blocks[-1].append(line)

    maps = [Map(b) for b in blocks]

    locations = []
    for s in seeds:
        value = s
        for m in maps:
            value = m.convert(value)
        locations.append(value)

    print(min(locations))


if __name__ == "__main__":
    main()
