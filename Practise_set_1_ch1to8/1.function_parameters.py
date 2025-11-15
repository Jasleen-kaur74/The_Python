"""Function with Parameters (Scaling):
Write a Python function named scale_data that accepts two parameters: a data point x and a scaling factor s.
 The function should return the result of x*s"""
#Function Definition
def scale_data(x,s):
    return x*s


#input from the user
x=int(input("Enter a number pls : "))
s=int(input("Enter the scaling number pls : "))


#calling the fucntion
print(f"The result of the scaling of the number is : {scale_data(x,s)}")

