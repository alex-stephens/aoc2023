def calibration_value(string):
    out = ""
    for c in string:
        if c.isdigit():
            out += c

    return int(out[0] + out[-1])


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    ans = sum(calibration_value(line) for line in lines)
    print(ans)


if __name__ == "__main__":
    main()
