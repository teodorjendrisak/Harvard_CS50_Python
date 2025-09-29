import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    try:
        filename = sys.argv[1]
        line_count = 0
        with open(filename) as file:
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    continue
                else:
                    line_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_count)


if __name__ == "__main__":
    main()