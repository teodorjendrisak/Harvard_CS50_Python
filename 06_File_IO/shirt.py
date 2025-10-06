import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input = sys.argv[1]
    output = sys.argv[2]

    valid_ext = (".jpg", ".jpeg", ".png")
    if not input.lower().endswith(valid_ext) or not output.lower().endswith(valid_ext):
        sys.exit("Invalid input")

    if os.path.splitext(input)[1] != os.path.splitext(output)[1]:
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input)
    except FileNotFoundError:
        sys.exit("File not found")

    shirt = Image.open("shirt.png")
    resize = ImageOps.fit(image, shirt.size)
    resize.paste(shirt, (0, 0), shirt)
    resize.save(output)

if __name__ == "__main__":
    main()