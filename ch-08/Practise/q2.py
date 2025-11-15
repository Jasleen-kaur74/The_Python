#2. Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(x):
    y = (x*(9/5))+32
    print(f"The conversion is : {y}")

celcius=int(input("Enter the temperature in degree celcius: "))
c_to_f(celcius)
