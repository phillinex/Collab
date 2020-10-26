import math

# a function to ensure entry is a valid number
def AcceptOnlyNumber():
    n = False #This will be return incase 'x' is entered
    while True:
        #This loop continues so long as entry is not valid
        try:
            entry=input("Enter a valid number or 'x' to cancel: ")
            if entry == 'x':
                break
            else:
                n = int(entry) 
            break
        except ValueError:
            print(str(entry) + " is not a valid number, please try again")
            continue
    return n

def factor(a):
    x=2 #Skipping the numbers 1 and the number itself 'a'
    for i in range(2, math.ceil(a/2)+1):
        if a%i==0:
            x+=1
    return x

#let the function that accepts only valid numbers handle the user entry    
num = AcceptOnlyNumber()

if num == False: #False is when the user enters x
    print("Thank you for passing by")
else:
    print(factor(num))



