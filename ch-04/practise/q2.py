#2. Write a program to accept marks of 6 students and display them in a sorted manner

student = []

s1 =int(input("Enter the student marks: "))
student.append(s1)

s2 =int(input("Enter the student marks: "))
student.append(s2)

s3 =int(input("Enter the student marks: "))
student.append(s3)

s4 =int(input("Enter the student marks: "))
student.append(s4)

s5 =int(input("Enter the student marks: "))
student.append(s5)

s6 =int(input("Enter the student marks: "))
student.append(s6)

student.sort()
print(student)