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

    def convert_range(self, seed_range):
        range_start, range_end = seed_range

        # Points where a range should *start*
        split_points = [range_start]

        # Go through each of the map ranges
        for _, source, range_ in self.ranges:
            if range_start <= source <= range_end:
                split_points.append(source)

            # One past the end
            if range_start <= source + range_ <= range_end:
                split_points.append(source + range_)

        split_points.append(range_end + 1)
        split_points = sorted(list(set(split_points)))  # remove duplicates
        split_ranges = [
            (split_points[i], split_points[i + 1] - 1)
            for i in range(len(split_points) - 1)
        ]

        output_ranges = []

        for split_range_start, split_range_end in split_ranges:
            new_start, new_end = self.convert(split_range_start), self.convert(
                split_range_end
            )
            output_ranges.append((new_start, new_end))

        return output_ranges


def main():
    filename = "input.txt"

    with open(filename) as f:
        seeds = list(map(int, f.readline().split(": ")[1].split()))
        lines = [line.strip() for line in f.readlines()]

    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    # Start and end values of ranges that need to be considered
    key_points = set()
    for start, end in seed_ranges:
        key_points.add(start)
        key_points.add(end)

    blocks = []
    for line in lines:
        if line == "":
            blocks.append([])
        else:
            blocks[-1].append(line)

    maps = [Map(b) for b in blocks]

    # Propagate the ranges through the maps
    for m in maps:
        updated_ranges = []
        for seed_range in seed_ranges:
            seed_range_converted = m.convert_range(seed_range)
            updated_ranges.extend(seed_range_converted)
        seed_ranges = updated_ranges

    print(min(seed_ranges)[0])


if __name__ == "__main__":
    main()
