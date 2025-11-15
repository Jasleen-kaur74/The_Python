name = "mustang"

# For the length of the string
print("Length of the string")
print(len(name))

#Does the string end with the given string
print('\n')
print("Ends with")
print(name.endswith("ang"))       #true
print(name.endswith("mus"))       #false

#Does the string starts with the given string
print('\n')
print("Starts with ")
print(name.startswith("ang"))       #false
print(name.startswith("mus"))       #true

#To capitalize
print('\n')
print("To capitalize")
print(name.capitalize())