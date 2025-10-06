import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r'src="https?://(www\.)?youtube\.com/embed/(\w+)"', s)
    if link:
        return (f"https://youtu.be/{link.group(2)}")
    else:
        return None


if __name__ == "__main__":
    main()