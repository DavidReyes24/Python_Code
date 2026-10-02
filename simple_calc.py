import math

def main():
    days = 30
    amount = 0.01
    value = doubleit(days, amount)
    print(f"{value:,}")

    goal = 1000000
    print(whenisitworthit(goal))




def doubleit(days, amount):
    for _ in range(days):
        worth = 2 * amount
        amount = worth

    return worth

def whenisitworthit(amount):
    worth, days = 0, 0
    value = 0.01
    while worth < amount:
        worth = 2 * value
        value = worth
        days += 1
    
    return math.ceil(days)

if __name__ == "__main__":
    main()