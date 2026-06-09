# We are going to convert pounds to kilograms by writing a program

# INPUT (get data that will be processed)
# Prompt user to enter weight in pounds
# validate user data: ensure the data is a number and not a string
# if the input in invalid then reprompt the user until the data is valid

# loop to validate user input
def get_positive_float_input():
    while True:
        try:
            input_weight = float(input("Enter your weight in pounds: "))
            # check if weight is <= 0, then output error messsage and reprompt user
            if input_weight <= 0:
                print("Invalid input. Please enter a number greater than zero. \n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.\n")
            continue
    return input_weight

#new definintion
def main():
        # INPUT (get data that will be processed)

    input_weight = get_positive_float_input()
        # Processing
        # Use a conversion factor to convert pounds to kilograms (1 pound = 0.453592 kilograms OR 1 kilogram = 2.20462 pounds)
    conversion_factor = 2.20462
    weight_in_kilograms = input_weight / conversion_factor

        # Output
        # Print output to user
    print(f"Your weight in kilograms is: {weight_in_kilograms:.3f} kg.")
main()