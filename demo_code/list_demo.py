def main():
    #create a list of strings, integers, and differing values
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_integers = [10, 16, 24, 42, 14, 9]
    random_type_list = ["Cyd", 15, 22.3, True, "Franck"]
    empty_list = []

    #print a list
    print(list_of_integers)

    #add values to a list
    print("\nAdding values to a list\n----------------")
    names.append("Johnny")
    list_of_integers.append(63)
    list_of_integers.append(5)
    print("List_of_integers: {list_of_integers}")
    print("List of names: {names}")

    #get the number of  items in a list
    print("\nGet the number of items in a list\n----------------")
    print(f"Items in integer list: {len(list_of_integers)}")
    print(f"Items in names list: {len(names)}")
    print(f"Items in empty list: {len(empty_list)}")

    #get values at specific indexes
    print("\nGet values at specific indexes in a list\n----------------")
    print(f"First item in names list: {names[0]}")
    print(f"Fourth item in names list: {names[3]}")

    #print all items in a list
    print("\nPrinting all names\n------------")
    for name in names:
        print(name)

    #print all items with index values
    print("\nPrinting all names with index values\n------------")
    for index in range(len(names)):
        print(f"names [{index}] = {names[index]}")

    #calculate the sum of all values in a list
    sum_of_all_integers = 0
    for number in list_of_integers:
        sum_of_all_integers += number
    print(f"Sum of all integers: {sum_of_all_integers}")

    #calculate the average of all integers in list
    avg_of_all_integers = sum_of_all_integers / len(list_of_integers)
    print(f"Average of all integers: {avg_of_all_integers:.2f}")

    #does the list contain a specific item
    search_name = "Veronica"
    if search_name not in names:
        print(f"{search_name} is not in the names list.")
    else:
        print(f"{search_name} is in the names list.")

    #find the largest values in a list
    #set max_value to the value of the first item in the list
    max_value = list_of_integers[0]

    #loop over the entire list
    for current_value in list_of_integers:
        #if current value > max_value, set max_value to current value
        if current_value > max_value:
            max_value = current_value

    #after loop is done, print the largest value
    print(f"\nList of integers: {list_of_integers}")
    print(f"Largest value in list: {max_value}")





main()