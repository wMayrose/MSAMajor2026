# Create a decision structure to determine the season: winter (dec to feb), spring (mar to may), summer (jun to aug), fall (sep to nov)
# Ask the user to enter the date
# Month must be 1-12
# Prompt: enter month number

def month_number():
    while True:
        try:
            month_number = float(input("Enter the month number: "))
            # check if number is between 1 to 12
            if month_number <= 0 or month_number > 12:
                print("Invalid input. Please enter a number greater than zero and less than or equal to 12. \n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours.\n")
            continue
    return month_number



# Output: It is (season)
def main():

    month = month_number()

    if month == 12 or month == 1 or month == 2:
        print(f"It is winter.")
    elif month == 5 or month == 4 or month == 3:
        print(f"It is spring.")
    elif month == 8 or month == 7 or month == 6:
        print(f"It is summer.")
    elif month == 11 or month == 10 or month == 9:
        print(f"It is fall.")


main()
