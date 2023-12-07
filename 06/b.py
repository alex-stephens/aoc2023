from math import sqrt, floor, ceil


def ways_to_win(t, d):
    # Accelerating for a seconds gives a score of (t-a)*a = at - a^2
    # So we need a^2 - at + d < 0
    # a = (t +- sqrt(t^2 - 4d)) / 2

    a1 = ceil((t - sqrt(t**2 - 4 * d)) / 2)
    a2 = floor((t + sqrt(t**2 - 4 * d)) / 2)

    return a2 - a1 + 1


def main():
    filename = "input.txt"

    with open(filename) as f:
        time = int("".join(f.readline().split(": ")[1].split()))
        dist = int("".join(f.readline().split(": ")[1].split()))

    print(ways_to_win(time, dist))


if __name__ == "__main__":
    main()
