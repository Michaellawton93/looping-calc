

#defining FUNCTIONS


##########################################################################################


#MAIN MENU FUNCTION this is what the user is presented with at beginning of program
def mainMenu():

#user input
    global calc
    calc = str(input("enter 1 for sum calculation 2 for product calculation 3 for exponent calculation 4 for modulus calculation or q to quit: "))

#prompt for valid input if user input is invalid
    while(calc != "1" and calc != "2" and calc != "3" and calc != "4" and calc != "q"):
        calc = str(input("enter 1 for sum calculation 2 for product calculation 3 for exponenet calculation 4 for modulus calculation or q to quit: "))
        if(calc == "1" or calc == "2" or calc == "3" or calc == "4" or calc == "q"):
            break


#SUM FUNCTION that is called when 1 is entered at main menu
def sum(x,y):
    sumAns = x + y
    print(sumAns)
    return sumAns


#PRODUCT FUNCTION that is called when 2 is entered at main menu
def prod(x,y):
    productAns = 0
    for i in range(0, y):
        productAns += x 
    print(productAns)
    return productAns


#EXPONENTIAL FUNCTION that is called when 3 is entered at the main menu

def exp(x,y):
    ans = 0

    for i in range(0, x):
        ans += x

    for i in range(0, y - 2):
        ans = ans * x
    print(ans)
    return(ans)

#MODULUS FUNCTION that is called when 4 is entered at the main menu

def modulo(x,y):
    while(x > 0 and y > 0):

        while(0 <= x + (-y)):
            x = x + (-y)
        print(x)
        return(x)
       



###################################################################################################




#MAIN BODY OF CODE

#####################################################################################################

#calling mainMenu function
mainMenu()


#if q is entered at the mian menu then program quits
if(calc == "q"):
    print("goodbye!")
    quit()

    
while(calc.isnumeric):

#ADDITION this is executed if the user enters 1 at main menu
    while(calc == "1"):
        firstNum = input("enter first positive number: ")
        secondNum = input("enter second positive number: ")

    #while loop is executed only if both firstNum or secondNum contain invalid input e.g. anything other than numeric input
        while(firstNum.isalpha() or secondNum.isalpha()):
            print("one of the inputted values was invalid")
            firstNum = input("enter first number again: ")
            secondNum = input("enter second number again: ")
    
    #while loop is executed only if both firstNum and secondNum contain valid input e.g. both are numeric
        while(firstNum.isnumeric() and secondNum.isnumeric()):
            x = int(firstNum)
            y = int(secondNum)
            sum(x,y)
            break
        mainMenu()



        
#PRODUCT this is executed if the user enters 2 at the main menu
    while(calc == "2"):
        x = int(input("enter the first positive number: "))
        y = int(input("enter the second positive number: "))
        productAns = 0


        while(x < 0 or y < 0):
            x = int(input("enter the first positive number: "))
            y = int(input("enter the second positive number: "))

    
        while(x > 0 and y > 0):
            prod(x,y)
            break
        mainMenu()


#EXPONENT this is executed if the user enters 3 at the main menu
    while(calc == "3"):
        x = int(input("enter the base as a positive number: "))
        y = int(input("enter the exponent as a positive number: "))
    
        while(x <= 0 or y <= 0):
            x = int(input("enter the base as a positive number : "))
            y = int(input("enter the exponent as a positive number: "))

        while(x > 0 and y > 0):
            exp(x,y)
            break
        mainMenu()


#MODULUS this is executed if the user enters 4 at the main menu
    while(calc == "4"):
        x = int(input("enter the numerator as a positive number: "))
        y = int(input("enter the denominator as a positive number: "))

     

        while(x <= 0 or y <= 0):
            x = int(input("enter the numerator as a positive number: "))
            y = int(input("enter the denominator as a positive number: "))


        while(x > 0 and y > 0):
            modulo(x,y)
            break
        mainMenu()
            

        