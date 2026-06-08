# Print Hello World
print("Hello World")

# create a variable to store my name
first_name = "Willa"

# create a variable for the last name
last_name = "Mayrose"

# write a python statement to display "My fullname is firstname lastname"
print("My full name is", first_name, last_name, sep="---")

# print using the f string (string interpolation)
print(f"My full name is {first_name} {last_name}.")

# create a variable to store my age and weight
age = 16
weight = 115.7
half_age = age / 2

# print a sentence with name, age, and weight
print(f"My name is {first_name} {last_name}. \nI am {age} years old and I weigh {weight} pounds.")

#get and print the data type for age, weight, and half-age
print("\nChecking Data Types\n--------------------")
print(type(age))
print(type(weight))
print(type(half_age))


# write 3 statements using string interpolation (f string) to print descriptive sentences for the data types
#     print dsescriptive statistics for the data types
print(f"The data type for age is {type(age)}.")
print(f"The data type for weight is {type(weight)}.")
print(f"The data type for half_age is {type(half_age)}.")


number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"The total of {number_1} and {number_2} is {total}.")