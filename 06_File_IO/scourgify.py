import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        filename_before = sys.argv[1]
        filename_after = sys.argv[2]
        with open(filename_before) as before_file:
            reader = csv.DictReader(before_file)
            student_data = list(reader)
    except FileNotFoundError:
        sys.exit(f"Could not read {filename_before}")

    with open(filename_after, "w", newline="") as after_file:
        writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in student_data:
            full_name = student["name"]
            last_name, first_name = full_name.split(", ")
            house = student["house"]
            writer.writerow({"first": first_name, "last": last_name, "house": house})

if __name__ == "__main__":
    main()