#1. Write a program to print multiplication table of a given number using for loop.
a = int(input("Enter the number pls: "))

for i in range(1,11):
    print(f"{a}*{i}=",a*i)