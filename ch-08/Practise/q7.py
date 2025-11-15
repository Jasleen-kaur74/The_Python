#7. Write a python function to remove a given word from a string and strip it at the same time.
def remove(string,word):
    string = string.replace(word,"")
    print(string.strip())

s = input("Enter the word pls: ")
a = input("Enter the word u want to remove and strip : ")

remove(s,a)