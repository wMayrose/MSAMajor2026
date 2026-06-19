from Student import Student

def main():

    #open students.csv: create a file handler to open file in read mode
    data_file = open("students.csv", "r")
    print(data_file)

    #create an empty dictionary
    student_info = {}

    #use loop to read contents of file line by line
    for line_of_data in data_file:

        #split the line at the comma
        all_student_data = line_of_data.split(",")
        print(all_student_data)

        #get the item and price from the list
        item_first_name = str(all_student_data[0])
        item_last_name = str(all_student_data[1])
        item_major = str(all_student_data[2])
        item_credit_hours = float(all_student_data[3])
        item_GPA = float(all_student_data[4])
        item_ID = str(all_student_data[5])


        #create an entry in the dictionary for the item and price
        student_info[item_name] = item_price

    #close the file
    data_file.close()

    #print all entries from the dictionary
    for first_name, last_name, major, credit_hours, GPA, ID in student_info.items():
        print(f"{first_name} {last_name}")
        print(f"Class level: {self.get_class_level()}, Major: {major}")
        print(f"GPA: {GPA}, ID: {ID}\n")



main()