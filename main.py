import math
def factor(a):
    x=0
    for i in range(1,ceil(a//2)):
        if a%i==0:
            x+=1
    return x
num=int(input("Enter number:"))
print()


