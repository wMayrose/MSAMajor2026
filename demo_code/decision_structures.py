def main():
    a = 7
    b = 4


    if a > b:
        print(f"a = {a} is greater than b = {b}.")
    elif b > a:
        print(f"b = {b} is greater than a = {a}.")
    elif a == b:
        print(f"a = {a} is equal to b = {b}.")


# print the appropriate letter grade based off test score
    print("\nGrade Decision: 1\n------------")
    test_score = 83


    if test_score >= 90:
        print("Congratulations! You recieved an A.")
    elif test_score < 90 or test_score >= 80:
        print("Good job! You recieved a B.")
    elif test_score < 80 or test_score >= 70:
        print("Good effort! You recieved a C.")
    elif test_score < 70 or test_score >= 60:
        print("The improvement is there! You recieved a D.")
    else:
        print("Better luck next time! You recieved an F.")


    print("\nGrade Decision: 1\n------------")



    if test_score >= 90:
        print("Congratulations! You recieved an A.")
    elif test_score >= 80:
        print("Good job! You recieved a B.")
    elif test_score >= 70:
        print("Good effort! You recieved a C.")
    elif test_score >= 60:
        print("The improvement is there! You recieved a D.")
    else:
        print("Better luck next time! You recieved an F.")

    c = 4
    d = 10

    if a == 4 or b == 5 or c == 5 or d == 9:
        print("The OR condition is true.")
    else:
        print("The OR condition is false.")


    main()