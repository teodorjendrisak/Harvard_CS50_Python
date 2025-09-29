def main():
    user_input = str(input("Input: "))
    print(shorten(user_input))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    user_output = ""

    for letter in word:
        if letter not in vowels:
            user_output += letter

    return user_output

if __name__ == "__main__":
    main()