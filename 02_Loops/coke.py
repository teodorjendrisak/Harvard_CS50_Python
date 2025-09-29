def main():
    amount_due = 50
    
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue
        if coin in [25, 10, 5]:
            amount_due -= coin
        
    if amount_due <= 0:
        change = abs(amount_due)
        print(f"Change Owed: {change}")

main()