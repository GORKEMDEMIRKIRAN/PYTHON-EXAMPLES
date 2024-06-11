


#CALCULUS MACHINE

## It performs the mathematical operations that the user wants to perform.
## The user enters 2 numbers and performs operations according to the number he has selected.


first_number=float(input("Enter first number: ")) 
second_number=float(input("Enter second number: "))
print("Please enter the process number:\n"
       "1-Addition\n"
       "2-Extraction\n"
       "3-Multiplication\n"
       "4-Division\n"
      )
point=input("Enter the transaction number you want to make a transaction: ")
if(point != float):
    if (point=="1"):
        print(first_number+second_number)
    elif (point=="2"):
        print(first_number-second_number)
    elif (point=="3"):
        print(first_number*second_number)
    elif (point=="4"):
        print(first_number/second_number)
else:
    print("Please enter the a valid transaction number.")
    


