#Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55  and goes on ......


def fib(n):
    #Here n is the number of the term that is nth term
    if(n==1 or n==2):          #this is the base condition 
        return(n-1)
    return fib(n-1)+fib(n-2)

n = int(input("Enter ur number for which term you want to print: "))
print(f"The number is : {fib(n)}")