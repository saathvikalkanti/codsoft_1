# Calculator application for basic arithmetic operations.
# Saathvik Alkanti / CodSoft Intern Task 2


while True: 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    oppChoice = input("Choose an opperation (+, -, *, /, %): ")

    if oppChoice == ("*"):

        print ("This opperation is equal to : ", num1 * num2)
    
    elif oppChoice == ("-"):

        print ("This opperation is equal to : ", num1 - num2)

    elif oppChoice == ("+"):

        print ("This opperation is equal to : ", num1 + num2)

    elif oppChoice == ("/"):
    
        if num2 == 0:
            print("Error: Cannot divide a number by zero")
        else:
            print("This opperation is equal to : ", num1 / num2)

    elif oppChoice == ("%"):

        print("This opperation is equal to : ", num1 % num2)

    else:
        print("Invalid operation. Please try again.")

    answer = input("Do you want to perform another opperation? (y/n): ").lower()


    if answer == "n":
    
        print("Bye!")
        break  