#Create a program in python called adding_game.py that prompts a user to answer a series of addition problems. 

#The program will keep track of the number of correct and incorrect answers and display the result at the end.
#The program should prompt the user for a difficulty level. Valid options are 1, 2, or 3.If the user does not input 1, 2, or 3, the program should prompt again.
#The program should prompt the user for a difficulty level. Valid options are 1, 2, or 3.If the user does not input 1, 2, or 3, the program should prompt again.
#The program should prompt the user for the number of questions to ask. Valid options are 3 - 10.If the user does not input 3 - 10, the program should prompt again.
#The program should randomly generate the number of questions the user entered in the previous step. 
    #For example, if the user entered 5 for the number of questions the program should ask, the program should then generate 5 math problems. 
    #Likewise, if they entered 10 the program should generate 10 problems. The problems should be formatted as X + Y = , wherein each of X and Y is a non-negative integer with difficulty level of digits. 
    #For example:
        #If the user chose difficulty level 1 then X and Y should be 1 digit, non-negative, numbers (0 - 9).
        #If the user chose difficulty level 2 then X and Y should be 2 digit, non-negative, numbers (10 - 99).
        #If the user chose difficulty level 3 then X and Y should be 3 digit, non-negative, numbers (100 - 999).
#Your program does not need to support operations other than addition (+).
#The program should prompt the user to solve each problem.
#If an answer is correct the program should output CORRECT!!! and the prompt the user to answer the next question.
#If an answer is not correct (or not even a number), the program should output WRONG!!! and prompt the user again, allowing the user up to three tries in total to answer the question. 
    #If the user has still not answered correctly after three tries, the program should output the correct answer and the prompt the user to answer the next question.

#The program should ultimately output the user’s score and the percentage (formatted to 2 decimal places) correct.
#End the program

#You must write at least 2 functions in your program. Consider writing the following functions:
    #function to get the game level from the user
    #fucntion to get the number of questions#


import random


#write difficulty level function
def difficulty():
    while True:
        try:
            difficulty_level = int(input("\nDifficulty Level (1, 2, 3): "))
            if difficulty_level == 1 or difficulty_level == 2 or difficulty_level == 3:
                break
            else:
                print("ERROR. Invalid input")
                continue
        except ValueError:
        # print error message and continue
            print("ERROR. Invalid input.")
            continue

        
    return difficulty_level


#write number of questions function
def number_questions():
    while True:
        try:
            number_of_questions = int(input("Number of Questions (3-10): "))
            if 3 <= number_of_questions <= 10:
                break
            else:
                print("ERROR. Invalid input.")
            continue
        except ValueError:
        # print error message and continue
            print("ERROR. Invalid input.")
            continue
    return number_of_questions



#main function
def main():
    #call functions
    difficulty_level = difficulty()
    number_of_questions = number_questions()
    questions_correct = 0

    for _ in range(number_of_questions):
        if difficulty_level == 1:
            x = (random.randint(1, 9))
            y = (random.randint(1, 9))
        elif difficulty_level == 2:
            x = (random.randint(10, 99))
            y = (random.randint(10, 99))
        elif difficulty_level == 3:
            x = (random.randint(100, 999))
            y = (random.randint(100, 999))



        # write math equations
        for math in range(3):
            try:
                answer = int(input(f"\n{x} + {y} = "))
                
            except ValueError:
                print("WRONG!!")
                continue

            if answer == x + y:
                print("CORRECT!!")
                questions_correct += 1
                break

            else:
                print("WRONG!!")
                continue
    percentage = questions_correct / number_of_questions * 100
    print(f"\n\nYou got {percentage:.1f}% or {questions_correct} out of {number_of_questions} correct.")

    if percentage <= 60.0:
        print("Better luck next time!\n")
    elif 60.0 < percentage <= 85.0:
        print("Good effort!\n")
    elif percentage > 85.0:
        print("Great job!\n")
        


main()