# A vending machine sells snacks for 50 cents. In a project named vending_machine.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# The user should only be able to input integers. Accepted denominations for coins are (1, 5, 10, 25). 
# The program should ignore any integer that isn’t an accepted denomination.

# Display the amount due
# Prompt the user to enter a coin
# Accepted denominations for coins are (1, 5, 10, 25)
# Program should ignore any input that is not a valid input and re prompt the user to input a coin
# Process the input and display the updated amount due
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed
# End program




# establish accepted coins
# establish target value (50)
# while true (amount coins enterred is <= 50)
# within loop we need to add the variable of remaining money owed (50 - inputted coins)


# break when value exceeds 50


# switch to variable declaring change owed (inputted coins - 50 cents)



def main():

    accepted_coins = [1, 5, 10, 25]
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due} cents")

        try:
            coins = int(input(f"Insert coins: "))
        except ValueError:
        # ignores integers not in accepted denomination
            continue
        # subtracts inputted coins from original total (50)
        if coins in accepted_coins:
            amount_due -= coins
        elif amount_due <= 0:
            break
        else:
            continue
        
    change_owed = abs(amount_due)
    print(f"Change owed: {change_owed}")

main()
