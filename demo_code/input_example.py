# We are going to convert pounds to kilograms by writing a program

# INPUT (get data that will be processed)
# Prompt user to enter weight in pounds
import string


input_weight = float(input("Enter your weight in pounds: "))

# Validate the input to ensure it's a positive number and not a string
if input_weight < 0:
    print("Weight cannot be negative. Please enter a valid weight.")

# Processing
# Use a conversion factor to convert pounds to kilograms (1 pound = 0.453592 kilograms OR 1 kilogram = 2.20462 pounds)
conversion_factor = 2.20462
weight_in_kilograms = input_weight / conversion_factor

# Output
# Print output to user
print(f"Your weight in kilograms is: {weight_in_kilograms:.2f} kg.")