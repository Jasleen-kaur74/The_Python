def goodDay(name,ending="Thanks"):
    print("Good Day "+name)
    print(ending)

goodDay("Mustang")

#here we wrote goodDay("Mustang")
#this means here we didnt add naything for ending but if we run this code
#then we will still get the value as Good Day,Mustang thanks
#Cuz in the definition o the function we already wrote to keep ending = "thanks"
#which here is like default value and if we dont provide endning specifically
#or particulary then it will pick up the deafault value here which is thanks