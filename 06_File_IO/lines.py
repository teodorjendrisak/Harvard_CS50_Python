import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a python file")

    try:
        lines = []

        input = sys.argv[1]
        with open(input) as file:
            for line in file:
                lines.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in lines:
        #you left off here - checking if lines is empty

if __name__ == "__main__":
    main()