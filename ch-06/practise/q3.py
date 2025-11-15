"""3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams."""

a1 ="Make a lot of money"
a2="buy now"
a3="subscribe this"
a4="click this"

message = input("Enter ur message: ")

if((a1 in message) or (a2 in message) or (a3 in message) or (a4 in message)):
    print("It is a spam , BE CAREFULL")

else:
    print("It is safe")