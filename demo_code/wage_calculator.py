
# Write a Python 3 program called wage_calculator.py that accepts user input from the keyboard for the hours worked and hourly wage. 
# The program calculates the total wages for the year, assuming the person works 350 days per year and 12% taxes are deducted from the wages.

# Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
# The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.
# the user cannot work more than 24 hours in a day

def daily_hours():
    while True:
        try:
            input_hours = float(input("Enter the hours worked daily: "))
            # check if weight is <= 0, then output error messsage and reprompt user
            if input_hours <= 0 or input_hours > 24:
                print("Invalid input. Please enter a number greater than zero. \n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours.\n")
            continue
    return input_hours


def hourly_wage():
    while True:
        try:
            input_wage = float(input("Enter the hourly wage: "))
            # check if weight is <= 0, then output error messsage and reprompt user
            if input_wage <= 0:
                print("Invalid input. Please enter a number greater than zero and less than 24. \n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for wage.\n")
            continue
    return input_wage


# Calculate the yearly wage given the two inputs
def main():
    input_hours = daily_hours()
    input_wage = hourly_wage()
    hours_worked = input_hours * 350
    wages_before_taxes = hours_worked * input_wage
    tax_amount = "12%"
    wages_after_taxes = wages_before_taxes * .88

    print("Pay Advice \n----------")
    print(f"Yearly hours worked: {hours_worked:.2f}")
    print(f"Hourly wage: ${input_wage:.2f}")
    print(f"Annual wages before taxes: ${wages_before_taxes:.2f}")
    print(f"Tax amount: {tax_amount}")
    print(f"Annual wages after taxes: ${wages_after_taxes:.2f}")


main()



# Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
# It would help to first write down the mathematical formula needed to calculate the yearly wage
# 12% will be deducted from yearly earnings for taxes

# Print the a Pay Advice containing: hours worked, hourly wage, wages before taxes, tax amount, annual wages after taxes, money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places