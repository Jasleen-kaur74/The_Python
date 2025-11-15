#6. Write a python function which converts inches to cms.

def inch_to_cms(n):
    return(n*2.54)


i = int(input("Enter the inches pls : "))

print(f"The value of inches into cms is : {inch_to_cms(i)}")