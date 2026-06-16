def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    #print the names of the students with their scores
    print("Students and scores using the lists\n-------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
    }


    #print Bob and Jane's scores
    print("Print Bob and Jane's scores\n--------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])


    #print all the data in the student scores dictionary
    print("\nPrint all student data\n-------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")


#create a dictionary to store care information
#make, model, year, value, engine size
    car_1 = {"make": "Ferrari", "model": "F-50", "year": 2024, "value": 500000, "engine_size": 4.8}

    #get all the car information
    print("\nGet all car information\n-------------")

    for key, value in car_1.items():
        print(f"{key}: {value}")


        #add an entry to a dictionary
    car_1["transmission"] = "manual"
    car_2["transmission"] = "automatic"

    #create a second car
    car_2 = {"make": "Honda", "model": "Accord", "year": 2024, "value": 18000, "engine_size": 2.4}

    #create a list of dictionaries
    dictionary_list = [car_1, car_2]

    #display information for all cars
    print("\nDisplay information for all cars\n-------------")

    #loop over all the cars
    for car in dictionary_list:
        print("\nCar information\n--------------")

        #loop of the key, avlue pairs in the dictionary
    for feature, value in car.items():
        print(f"{feature}: {value}")


    #create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}

    #print all car in formation from the dictionary
    print("\nCar info from dictionaries\n-----------------")

    for make, car in car_dictionary.items():
        print(f"\n{make}")
        for feature, value in car.items():
            print(f"{feature}: {value}")

    
    #getting a value froma dictionary when no key exists
    key = "transmission"
    print("\nFinding key using try/except\n----------------")
    try:
        print(f"{car_1["key"]}")
    except:
        print(f"ERROR. Key '{key}' does not exist in the dictionary.")


    print(f"Finding key using dictionary.keys()\n-------------")
    if key not in car_1.keys():
        print(f"ERROR. Key '{key}' does not exist in the dictionary.")
    else:
        print(f"{car_1[key]}")















main()