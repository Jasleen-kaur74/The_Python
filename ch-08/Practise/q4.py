#4. Write a recursive function to calculate the sum of first n natural numbers.

def sum (n):
    if(n==1):
        return 1

    return((n)+sum(n-1))

a =int(input("Enter the number upto which u want the sum :"))
print(f"The sum is {sum(a)}")