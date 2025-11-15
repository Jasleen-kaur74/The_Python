#Recursion is a function which calls itself.

def factorial(n):
    if(n==1 or n==0):               # THIS IS THE BASE CONDITION WE NEED TO ADD
        return 1           #WITHOUT THIS THE CODE WILL GO UP TO INFINITY
    return n*factorial(n-1)

n = int(input("Enter a number pls : "))
print(f"The factorial of the number is : {factorial(n)}")