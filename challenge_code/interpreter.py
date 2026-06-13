#In a file called interpreter.py, implement a program: 
# takes an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer

# Prompt the user to enter a math expression in the format X y Z where y is a math operator (+, _, *, /)
# "Expression: "
def main():
    def expression():
        while True:
            try:
                expression_value = input("Expression: ")
                # check if X and Z are floats and prompt user to change them
                x, y, z = expression_value.split(" ")
                number1 = int(x)
                number2 = int(z)
                # set up math equations
                
                if expression_value[1] == float or expression_value[3] == float:
                    print("ERROR. Please enter an integer for X and Z. \n")
                    continue
                # check if Y is valid arithmetic method
                elif expression_value[2] != "+" or expression_value[2] != "-" or expression_value[2] != "*" or expression_value[2] != "/":
                    print("ERROR. Please enter a valid arithmetic method (+, -, *, /).")
                    continue
            except ValueError:
                print("ERROR. Incorrect expression format.\n")
                if y == '+':
                        result = number1 + number2
                elif y == '-':
                        result = number1 - number2
                elif y == '*':
                        result = number1 * number2
                elif y == '/':
                        result = number1 / number2
            return expression_value
    expression_value = expression()
main()


# Parse the expression to determine which operation to carry out and the value of the numbers
# If the expression is in an incorrect format, OUTPUT AN "Incorrect Format" and reprompt the user.
# Output the answer to the expression

