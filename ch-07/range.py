#range have three integer arguments : Start , Sop and Step

#range(stop)
#we have to convert it into a list or something to print here
#here it will stop before the integer we entered
print(list(range(7)))
# 8 is the stop integer argument
# Step here is increment by one which is deafult


#range(start,stop)
print(list(range(1,8)))
#here start is at one and the stop is at 8 and step by deafault is one


#range(start,stop,step)
print(list(range(1,11,1)))      #forward counting
print(list(range(10,0,-1)))      #backward counting