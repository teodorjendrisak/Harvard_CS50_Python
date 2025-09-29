def main():
    while True:
        try:
            user_fraction = str(input("Fraction: "))
            convert(user_fraction)
            answer = convert(user_fraction)
            print(gauge(answer))
            break
        except (ValueError, ZeroDivisionError):
             pass

def convert(fraction):
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y < 0 or x < 0 or x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            return int((x/y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()