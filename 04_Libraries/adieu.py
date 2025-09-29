import inflect


def main():
    names = []
    p = inflect.engine()
    
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass

    output = p.join(names[:])
    print(f"Adieu, adieu, to " + output)





if __name__ == "__main__":
    main()