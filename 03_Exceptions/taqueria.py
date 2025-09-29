menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order_prices = []

def main():
    while True:
        try:
            item = str(input("Item: ")).title()
            order_prices.append(float(menu_items[item]))
            print(f"${sum(order_prices):.2f}")

        except EOFError:
            print("\n")
            break
        except KeyError:
            pass

if __name__ == "__main__":
    main()