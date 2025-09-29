grocery_dict = {}


def main():
    while True:
        try:
            item = str(input()).upper()
            
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1
        except EOFError:
            break
        except KeyError:
            pass
    
    for item in sorted(grocery_dict):
        print(f"{grocery_dict[item]} {item}")


if __name__ == "__main__":
    main()