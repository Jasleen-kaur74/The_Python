def goodDay(name):                       # name is a parameter passed to the function
    print("Good Day "+name)
    return "done"

a=goodDay("Mustang")
print(a)
#now it will not give us any value cuz it does not return us any value
#Which means the goodDay is not returning us any value


# So we will say the function to the a value with it
# and if some varibale asks for it then give it to the variable
# so as we wrote return "done" then now if we print a then it have a value
#which is "Done"
#if it is 7 then 7 will get printed
"""With print() we cant use the value again but with return we can use the value again """

# we call any function many times as we wish
# we can add as many arguments we want such as def goodDay(name,ending)
# then we will call the function as
# goodDay("Mustang","Thanks")
