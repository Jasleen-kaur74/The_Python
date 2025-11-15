"""Looping and Counting (Data Filtering):
A list of feature values is feature_vals = [5, 10, 0, 22, 5, 0, 18].
Write a short for loop that iterates over this list and uses a conditional to
count how many times the value 0 appears. Print the final count"""

feature_vals = [5, 10, 0, 22, 5, 0, 18]    # list
count = 0
for i in feature_vals:              # for loop starts
    if(i==0):
        count +=1                   # to count


print(f"0 occurs : {count} times")     #printing the count

