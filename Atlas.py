#This section assigns variables to the numbers and the function inputed by a user
func=input("Enter a function(+,-,*,/):")
num1=float(input("Enter a number:"))
num2=float(input("Enter another number:"))
#This section processes the function and prints the result for each possible function
if func=="+":
    print(f"{num1}+{num2}={num1+num2}")
elif func=="-":
    print(f"{num1}-{num2}={num1-num2}")
elif func=="*":
    print(f"{num1}*{num2}={num1*num2}")
elif func=="/":
    print(f"{num1}/{num2}={num1/num2}")
