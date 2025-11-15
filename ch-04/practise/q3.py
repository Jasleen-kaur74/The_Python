#3. Check that a tuple type cannot be changed in python.
t1 = (7,8.8,"apple",False)

t1[2] = "mango"      # this will give us error cuz tuple is immutable
#and we cant assign the items