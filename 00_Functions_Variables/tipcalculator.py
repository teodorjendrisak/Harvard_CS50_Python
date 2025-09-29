# https://cs50.harvard.edu/python/2022/psets/0/tip/

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percentage_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d

def percentage_to_float(p):
    p = float(p.replace("%", "")) /100
    return p


main()