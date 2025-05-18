def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual percentage rate (as decimal): "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)