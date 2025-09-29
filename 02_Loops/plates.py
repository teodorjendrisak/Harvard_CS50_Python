def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return start_two_letters(s) and correct_length(s) and numbers_end(s) and special_character(s)


def start_two_letters(st):
    return st[:2].isalpha()
    
def correct_length(le):
    return 2 <= len(le) <= 6

def numbers_end(ne):
    for i, char in enumerate(ne):
        if char.isdigit():
            if not ne[i:].isdigit():
                return False
            if char == "0":
                return False
            break
    return True

def special_character(sc):
    for char in sc:
        if not (char.isdigit() or char.isalpha()):
            return False
    return True

main()
