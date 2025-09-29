def main():
    camel_case = str(input("camelCase: "))
    snake_case = ""

    for i in range(len(camel_case)):
        letter = camel_case[i]
        
        if letter.isupper():
            snake_case += "_" + letter.lower()

        else:
            snake_case += letter

    print(snake_case)

main()