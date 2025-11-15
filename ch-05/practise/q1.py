#1. Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!

translation={"kela":"Banana",
             "seb":"Apple",
             "amb": "Mango"}

word = input("Enter the name of the furit you want the translation of : ")
print(translation[word])