"""Conditional Logic (Model Evaluation):A machine learning model's accuracy is stored in the variable accuracy.
Write an if-elif-else block that checks the accuracy and prints:"Excellent" if accuracy is >= 0.95.
"Good" if accuracy is between $0.80$ (inclusive) and 0.95 (exclusive)."Needs Improvement" otherwise."""

#input from the user
a=(float(input("Enter the number to check the accuracy: ")))

#if-elif-else block
if(a>=0.95):
    print("Excellent")

elif(a<=0.80 ):
    print("Good")

else:
    print("Need Improvement")
