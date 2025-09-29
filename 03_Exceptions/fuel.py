def get_percentage():
    while True:
        try:
            user_fraction = str(input("Fraction: ")).split("/")
            x = int(user_fraction[0])
            y = int(user_fraction[1])
            percentage = int((x/y) * 100)

            if y <= 0:
                continue
            elif x < 0:
                continue
            elif x > y:
                continue
            else:
                return percentage

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def main():
    answer = get_percentage()
    if answer <= 1:
        print("E")
    elif answer >= 99:
        print("F")
    else:
        print(answer, "%", sep="")

if __name__ == "__main__":
    main()