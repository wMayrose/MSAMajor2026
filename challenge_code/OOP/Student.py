#Create a student Class with these attributes. Remember to use the __ to make them private (Create get/set methods where appropriate).
#First name, Last name, major, credit hours, gpa, ID number

#get_class_level: determine the class based on the students credit hours. Method will return:
    #"Freshman": 0 - 30 hours, "Sophomore": 31 - 60 hours, "Junior": 61 - 90 hours, "Senior": more than 90 hours

#update_credit_hours: 1 parameter for additional hours. This method will update credit hours by adding aditional_hours to the students credit hours.

#print_student_data: Print all student data in the following format
    #John Smith
    #Class Level: Junior, Major: Computer Science
    #GPA: 3.75, ID: 12345678



import datetime
class Student():
    #define constructor
    #the constructor is a function that is called to create a student profle
    def __init__(self, first_name:str, last_name:str, major:str, credit_hours:int, GPA:float, ID:str):
        #define class properties witht the parameter values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__GPA = GPA
        self.__ID = ID

    #create getter and setter methods for class properties
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_major(self):
        return self.__major
    

    def get_credit_hours(self):
        return self.__credit_hours
    

    def set_credit_hours(self, new_hours:int):
        self.__credit_hours = new_hours
        return


    def update_credit_hours(self, additional_hours:int):
        self.__credit_hours += additional_hours
        return
    

    def get_GPA(self):
        return self.__GPA
    

    def set_GPA(self, new_GPA:float):
        self.__GPA = new_GPA
        return
    
    def get_ID(self):
        return self.__ID
    
    #create a method to get a class level
    def get_class_level(self):
        if 0 <= self.__credit_hours <= 30:
            return "Freshman"
        elif 30 < self.__credit_hours <= 60:
            return "Sophomore"
        elif 60 < self.__credit_hours <= 90:
            return "Junior"
        else:
            return "Senior"


    #create a method to print student data
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__GPA}, ID: {self.__ID}\n")
        

    