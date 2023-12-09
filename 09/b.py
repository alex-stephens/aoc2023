def get_extrapolated_value(h):
    layers = [h]

    # Propagate
    while not all([x == 0 for x in layers[-1]]):
        layers.append(
            [layers[-1][i] - layers[-1][i - 1] for i in range(1, len(layers[-1]))]
        )

    # Extrapolate
    layers[-1] = [0] + layers[-1]
    for i in range(len(layers) - 2, -1, -1):
        layers[i] = [layers[i][0] - layers[i + 1][0]] + layers[i]

    return layers[0][0]


def main():
    filename = "input.txt"

    with open(filename) as f:
        histories = [list(map(int, line.strip().split())) for line in f.readlines()]

    ans = sum([get_extrapolated_value(h) for h in histories])
    print(ans)


if __name__ == "__main__":
    main()
