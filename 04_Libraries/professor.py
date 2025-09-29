import random


def main():
    level = get_level()
    score = 0
    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0
        correct_answer = x + y

        while attempts < 3:
                    try:
                        user_answer = int(input(f"{x} + {y} = ").strip())
                        if user_answer == correct_answer:
                            score += 1
                            break
                        else:
                            print("EEE")
                    except ValueError:
                        print("EEE")
                    attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()