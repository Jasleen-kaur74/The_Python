marks = {
    "Harry": 100,                # key : value
    "Shubam": 27,              #list of key value pairs
    "Rohan": 77,
}

#marks.items --> it gives the (key,value) items in tuples
print(marks.items())
print('\n')

#marks.keys() --> it gives the list of the keys of the dict
print(marks.keys())
print('\n')

#marks.values() --> it gives the list of the values of the dict
print(marks.values())
print('\n')

#marks.update() --> changes the values
marks.update({"Harry":96,"Renuka":145})
print(marks)               #this also proves that dictionary is mutable
print('\n')         #the key value pair which exixts in the dictionary gets updated and the value is changed
# and the ones which are not ther gets added at the end in the dictionary

#for the length of the dictionary we use(len)
print(len(marks))
print('\n')


#marks.get()  --> it gives the value of the specified keys
print(marks.get("Harry"))
print(marks["Harry"])     # so then what is the difference btw these two
print('\n')
# cuz if we write this as Harry2 instead of Harry then
#print(marks.get("Harry2"))  # but this will give us none
#print(marks["Harry2"]) # then this will give us key error

# marks.pop()  --> removes the specified key and returns the value
marks.pop("Rohan")
print(marks)
print('\n')

#marks.popitem()  --> removes the last added item from the dictionary
marks.popitem()
print(marks)

#the use of deafult value
default = marks.pop("sita","not found")
print(default)
# here if havent added the deafult thingy then it will return us an error
#cuz the key word doesnt exixts
#so now we added the deafut thingy then it wont give us the error