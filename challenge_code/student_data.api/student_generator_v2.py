from Student import Student
from datetime import datetime

"""
Function to write an error message to a log file
Input: the error message (string)
Output: none
"""
def write_to_error_log(message:str) -> None:
    the_date = datetime.now()

    #open the log file in append mode: error_log.txt
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{the_date}: {message}\n")
        #write an error message to the file in the format 6/26/2026: Error in data file on line 5.
    return

"""
Function to return a list of student objects
Input: none
Output: list of student objects
"""




def load_students() -> list[Student]:

    #open students.csv: create a file handler to open file in read mode
    data_file = open("students.csv", "r")


    #create an empty list
    student_info = []

        #use loop to read contents of file line by line
    for line_of_data in data_file:
        
        #split the line at the comma
        all_student_data = line_of_data.split(",")

        try:
            #handle errors in data format. line_of_data should have 6 items
            #if error in format than write to a log file
            if len(all_student_data) != 6:
                write_to_error_log(f"ERROR in the file. Data has {len(line_of_data)} items but should have six.")
                raise Exception(f"ERROR in the file. Data has {len(line_of_data)} items but should have six.\n")
        except Exception as error:
            continue

        try:
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

    return student_info

"""
Function to convert student objects into dictionaries
Input: list of student objects
Output: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create an empty list to store the dictionaries
    student_dictionary_list = []

    #loop through the list and write each students' data to a dictionary
    for student in list_of_students:

        #create an empty dictionary
        student_dictionary = {}

        #make entries into the dictionary using the student properties
        #firstname, lastname, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['GPA'] = student.get_GPA()
        student_dictionary['ID'] = student.get_ID()

        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)

    #return list of dictionaries
    return student_dictionary_list



"""
Functions to get student dictionaries
Input: none
Output: a list of student dictionaries
"""

def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

get_student_dictionaries()