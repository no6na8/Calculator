#Developed by Noorah Albuainain
#-------------------------------------------
def calc(choice,x,y):
    if choice == '1':
        result = x + y
        print(x, "+", y, "=" , result)

    elif choice == '2':
        result = x - y
        print(x, "-", y, "=", result)

    elif choice == '3':
        result = x * y
        print(x, "*", y, "=", result)

    elif choice == '4':
            try:
                result = x / y
                print(x, "/", y, "=", result)
            except ZeroDivisionError as e:
                print (e)
    else :
        print ("Invalid option")
#-------------------------------------------         
        
i = 0 
while (i!=5):
    print ("1. Add \n2. Subtract\n3. Multiply \n4. Divide \n5. Exit ")
    i = input ("Choose the opertion to calcualte it: ")
    x = float(input ("Enter the first number "))
    y = float(input ("Enter the second number "))
    calc (i,x,y)
