#8. Write a python function to print multiplication table of a given number

def multiplication (n):


    for i in range (1,11):
        product= n*i
        print(f"{n} X {i:2} = {product}")       # we wrote this :2 for the equal spacing here


n = int(input("Enter the number pls: "))
multiplication(n)