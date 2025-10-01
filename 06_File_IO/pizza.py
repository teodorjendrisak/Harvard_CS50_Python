from tabulate import tabulate
import sys
import csv


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        filename = sys.argv[1]
        with open(filename) as file:
            reader = csv.DictReader(file)
            menu_items = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(menu_items, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
