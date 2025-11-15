#6. Write a program to calculate the factorial of a given number using while loop.
n = int(input("Enter the number:"))
i=1
fac=1
while(i<=n):
    fac *= i
    i += 1

print(f"The value of factorial is : {fac}")
