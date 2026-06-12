def main():
    my_name = "willa"

# capitalize the string
    print(f"My name capitalized: {my_name.capitalize()}")
# make a string uppercase
    print(f"My name uppercase: {my_name.upper()}")
# make a string lowercase
    last_name = "Mayrose"
    print(f"My full name lowercase: {my_name.lower()} {last_name.lower()}")
# compare two strings
    my_name_title_case = "Willa"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal.")

    
    print("Using the Startswith() Method\n---------------------")
    #determine if a string starts with a set of characters
    print(f"{my_name} starts with a W or w: {my_name.startswith("W") or my_name.startswith("w")}")


    if(not my_name.startswith("Wil") and (not my_name.startswith("wil"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")

    print("\nUsing the Endswith() Method\n--------------")
    print(f"{my_name} ends with 'la': {my_name.endswith('la')}")

    # find i in Willa
    print("\nUsing the Find() Method\n------------------")
    search_letter = "l"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")
    else:
        print(f"There is no '{search_letter}' in {my_name}")


    print("\nLooping through a string\n---------------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters.")
    # print the letters in a string along with the index positions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\nSearch a string\n-------------")
    sentences = "I have a dog. My dog is cute. Do you want a dog?"
    # Write code that counts the number of occurances of the word 'dog' in the sentence
    # Expected output: 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        # start at the beginning of the string
        # search for the occurance of the word "dog" starting at index 0
        dog_index = sentences.find(search_word, start_index)
        # if we find dog, add 1 to some variable we use to keep track of the numbers of dogs we find
        # continue searching the string from the next index after the dog we just found
        # update the starting index by 1
        if dog_index == -1:
            break
        else:
            # number_of_dogs = number_of_dogs + 1
            number_of_dogs += 1


            # update the starting index by 1
            start_index = dog_index + 1
        # do this until we don't find any more dogs (-1 is returned to the console)
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")

main()