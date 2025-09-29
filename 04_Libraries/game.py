import random

def main():
    n = valid_input()
    answer = random.randint(1, n)

    while True:
        guess = guess_input()
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break

def guess_input():
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess > 0:
                return guess
        except ValueError:
            pass

def valid_input():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level > 0:
                return level
        except ValueError:
            pass


if __name__ == "__main__":
    main()