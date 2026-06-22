from Student import Student

def main():

    #open students.csv: create a file handler to open file in read mode
    data_file = open("students.csv", "r")
    print(data_file)

    #create an empty list
    student_info = []

        #use loop to read contents of file line by line
    for line_of_data in data_file:

        try:
            #handle errors in data format. line_of_data should have 6 items
            #if error in format than write to a log file
            if len(line_of_data) != 6:
                raise Exception(f"ERROR in the file. Data has {len(line_of_data)} items but should have six.")
        except Exception as error:
            continue

        try:

            #split the line at the comma
            all_student_data = line_of_data.split(",")
            print(all_student_data)

            #get the pieces of data from the list
            first_name = all_student_data[0]
            last_name = all_student_data[1]
            major = all_student_data[2]
            credit_hours = int(all_student_data[3])
            GPA = float(all_student_data[4])
            ID = all_student_data[5].strip()

            #create a student object
            student1 = Student(first_name, last_name, major, credit_hours, GPA, ID)
            student_info.append(student1)
        except:
            print(f"INDEX ERROR.")
            continue
  
    #close the file
    data_file.close()

    #print all items from the list
    for student in student_info:
        student.print_student_data()
    
        #print(f"{first_name} {last_name}")
        #print(f"Class level: {self.get_class_level()}, Major: {major}")
        #print(f"GPA: {GPA}, ID: {ID}\n")



main()