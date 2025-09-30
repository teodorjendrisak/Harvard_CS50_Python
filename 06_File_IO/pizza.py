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
        menu_items = []

        filename = sys.argv[1]
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu_items.append({"pizza": row["Sicilian Pizza"], "small": row["Small"], "large": row["Large"]})
                #Still need to change so also first line get's printed (check header option) and change the table style
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(menu_items))


if __name__ == "__main__":
    main()