list = ["apple","mustang",7.7, 21,False]

#append() ----> add at the end            list.append( the_thing_u_want_to_add )
list.append("Ford")
print("Append ")
print(list)

print('\n')
#sort --> it arranges them in a ascending order if we have numbers
l2 = [1,23,45,75,7]
l2.sort()
print("Sort")
print(l2)

print('\n')
#reverse ---> it reverses the elements of the list
list.reverse()
print("Reverse")
print(list)

print('\n')
#insert()---> adding at an index        list.insert(index_no. , the_thing_u_want_to_add)
list.insert(4,"lambo")
print("Insert")
print(list)

print('\n')
#pop() ---> will delete the element at the index     list.pop(index_no.)
print("Pop")
value = list.pop(2)
print(value)



print('\n')
#remove() --->  will delete the number          list.remove(element)
print("Remove")
l2.remove(45)
print(l2)
