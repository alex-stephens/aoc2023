DIGITS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "---",
}


def calibration_value(string):
    first_loc = {x: 1000 for x in range(10)}
    last_loc = {x: -1000 for x in range(10)}

    for d in range(10):
        # Digit
        if string.find(str(d)) != -1:
            first_loc[d] = min(first_loc[d], string.find(str(d)))
            last_loc[d] = max(last_loc[d], string.rfind(str(d)))

        # Word
        if string.find(DIGITS[d]) != -1:
            first_loc[d] = min(first_loc[d], string.find(DIGITS[d]))
            last_loc[d] = max(last_loc[d], string.rfind(DIGITS[d]))

    first = min(first_loc, key=first_loc.get)
    last = max(last_loc, key=last_loc.get)

    return int(str(first) + str(last))


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    ans = sum(calibration_value(line) for line in lines)
    print(ans)


if __name__ == "__main__":
    main()
