#Create a program that prompts the user to input a menu item and calculate the total for the order.
#There is a restaurant which offers a menu of entrees, per the list of items and prices below.


#In a program called menu.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user types the word "end". 
#After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
#Ignore any input that isn’t an item. You should create the menu as a dictionary.


#Prompt user for an item
#Display the total cost of all items inputted prefixed with a dollar sign ($) formatted to two decimal places
#Ignore any input that isn’t an item. The case will matter; for example "Taco" is a valid key but "taco" is not. So the user must enter the item as it is stored in the dictionary
#End the program when user types "end". Case should not matter. If the user types "end", "END", "End", "eND"...etc the program should still end.
#Create the menu as a dictionary.


#Bonus: Assume all the items in the menu are in title case. Implement the program in a way such that if a user enters the item name in any case it will still fin the item. 
#Note: Your program should not crash for any reason. You should handle any exception(s) that may occur.

#function to load data from a file a return a dictionary
#input: filename
#output: dictionary
def load_menu_items(filename:str) -> dict:
    #open menu.txt: create a file handler to open file in read mode
    data_file = open(filename, "r")
    print(data_file)

    #create an empty dictionary
    menu_items = {}

    #use loop to read contents of file line by line
    for line_of_data in data_file:

        #split the line at the comma
        item_name_and_price = line_of_data.split(",")

        #get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price

    #close the file
    data_file.close()


    #return the dictionary of menu items
    return menu_items

#load_menu_items()








def main():

    menu_items = load_menu_items("menu.txt")

    running_total = 0.00

    while True:


        try:
            menu_choice = input(f"Item:\n").title()
        except ValueError:
        # ignores numbers and words not in dictionary
            continue
        # adds value of item to total
        if menu_choice in menu_items:
            running_total += (menu_items[menu_choice])
            print(f"Total: ${running_total:.2f}\n")
            continue
        elif menu_choice.lower() == "end":
            break
        else:
            continue
            



main()