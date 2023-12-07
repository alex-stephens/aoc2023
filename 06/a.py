def ways_to_win(time, distance):
    count = 0
    for a in range(time + 1):
        d = (time - a) * a
        count += 1 if d > distance else 0

    return count


def main():
    filename = "input.txt"

    with open(filename) as f:
        times = list(map(int, f.readline().split(": ")[1].split()))
        distances = list(map(int, f.readline().split(": ")[1].split()))

    ans = 1
    for t, d in zip(times, distances):
        ans *= ways_to_win(t, d)
    print(ans)


if __name__ == "__main__":
    main()
