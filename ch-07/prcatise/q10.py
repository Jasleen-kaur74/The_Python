"""10. Write a program to print multiplication table of n using for loops in reversed
order."""
a = int(input("Enter the number pls: "))

for i in range(10,0,-1):
    print(f"{a}*{i}=",a*i)