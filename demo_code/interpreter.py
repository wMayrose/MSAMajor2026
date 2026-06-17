#In a file called interpreter.py, implement a program: 
# takes an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer

# Prompt the user to enter a math expression in the format X y Z where y is a math operator (+, -, *, /)
# "Expression: "
def main():

    while True:
        try:
            expression_value = input("Expression: ")
            # check if X and Z are floats and prompt user to change them
            x, y, z = expression_value.split(" ")
            number1 = int(x)
            math_sign1 = (y)
            number2 = int(z)


            # set up math equations
            if y == '+':
                    result = number1 + number2
            elif y == '-':
                    result = number1 - number2
            elif y == '*':
                    result = number1 * number2
            elif y == '/':
                    if number2 == 0:
                        print("ERROR. Cannot divide by 0.")
                        continue
                    result = number1 / number2
            else:
                print("ERROR. Please enter a valid arithmetic method (+, -, *, /).")
        except ValueError:
            print("ERROR. Incorrect expression format. The correct format is: integer method integer\n")
            
        
        #print(f"Answer: {result:.1f}")

        try:
            print(f"Answer: {result:.1f}")

        except Exception as e:
            print(f"ERROR: {e}")

        opinion = input("Do you want to evaluate another expression? (Y or N): ").strip()
        if opinion == "Y":
            continue
        elif opinion == "N":
            break
        else:
            print("ERROR. Please enter Y (yes) or N (no).")
main()


# Parse the expression to determine which operation to carry out and the value of the numbers
# If the expression is in an incorrect format, OUTPUT AN "Incorrect Format" and reprompt the user.
# Output the answer to the expression

