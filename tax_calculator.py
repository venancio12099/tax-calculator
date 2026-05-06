def print_greeting():
    print("Welcome to Venancio's Tax Generator")
  
def get_details():  # Get the employee details
    full_name = input("Please, introduce your full name: ")
    organisation = input("Please indicate the name of your company: ")
    return full_name, organisation
 
def get_income():  # Get the income and send error if invalid input
    try:
        income = float(input("Please indicate your income: "))
        return income
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0.0
 
 
def calculate_tax_and_NetPay(income):
    if income <= 12500:
        tax_band = "Personal Allowance 0%"
        tax = 0
    elif income <= 50000:
        tax_band = "Basic Rate 20%"
        tax = (income - 12500) * 0.20
    elif income <= 150000:
        tax_band = "Higher Rate 40%"
        tax = (income - 50000) * 0.40 + (50000 - 12500) * 0.20 
    else:
        tax_band = "Additional Rate 45%"
        tax = (income - 150000) * 0.45 + (150000 - 50000) * 0.40 + (50000 - 12500) * 0.20

    net_pay = income - tax
    return tax_band, tax, net_pay
 
 
def print_payslip(full_name, organisation, income, tax_band, tax, net_pay):
    print("\n----Payslip----")
    print(f"Your full name: {full_name}")
    print(f"Organisation: {organisation}")
    print(f"Annual income: £{income:.2f}")
    print(f"Tax band: {tax_band}")
    print(f"Income tax: £{tax:.2f}")
    print(f"Net Pay: £{net_pay:.2f}")
    print("---------------\n")
 
 
def main():
    print_greeting()
    while True:
        full_name, organisation = get_details()
        income = get_income()
        tax_band, tax, net_pay = calculate_tax_and_NetPay(income)
        print_payslip(full_name, organisation, income, tax_band, tax, net_pay)
 
        another = input("Do you want to add another employee? (yes/no): ").strip().lower()
        if another != "yes":
            break
 
    print("Thank you for using Venancio's Tax Calculator services!")
 
 
if __name__ == "__main__":
    main()



