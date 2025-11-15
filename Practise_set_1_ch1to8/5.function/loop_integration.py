"""Function/Loop Integration (Data Aggregation): Write a function called calculate_total
that accepts a list of numbers, data_list.
Inside the function, use a for loop to sum all the numbers and return the final total."""

#function defintion

def calculate_total(data_list):
    total = 0                    #initializin total to 0
    for i in data_list:
        total += i
    return total                        # it return the value of total but we need to store it in another varibale
                                     #to print the value
data_list=[7,8,5,1,7]
sum = calculate_total(data_list)
print(f"The sum is : {sum }")


