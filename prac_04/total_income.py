def main():
    incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    total = 0
    print("\nIncome Report\n-------------")
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
