#1. Write a program using functions to find greatest of three numbers
def greatest(a,b,c):
    if(a>b and a>c):
        print(f"The greatest number is : {a}")

    elif (b > a and b > c):
        print(f"The greatest number is : {b}")

    elif (c > b and c > a):
        print(f"The greatest number is : {c}")


a = int(input("Enter ur first number: "))
b = int(input("Enter ur second number: "))
c = int(input("Enter ur third number: "))

greatest(a,b,c)