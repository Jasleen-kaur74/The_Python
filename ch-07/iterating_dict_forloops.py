#using for loop to iterate over a dictionary
student = {"name":"Mustang",
           "class":12,
           "subject":"maths"}

for x in student:
    print(x)

print('\n')
#Acessing values of a Dictionary

for x in student:
    print(student[x])
print('\n')

#we can also acess values of dictionary by using the value method
for y in student.values():
    print(y)
print('\n')


#for acessing keys of a dictionary by the keys() method
for z in student.keys():
    print(z)
print('\n')

#for accessing keys and values of a dictionary by using items() method
for j,k in student.items():
    print(j, k)
