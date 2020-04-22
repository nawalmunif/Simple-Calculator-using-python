print("******************SIMPLE CALCULATOR******************")

num1 = float(input("\n Enter first number: \n "))
num2 = float(input("\n Enter second number: \n "))

operator = int(input(" \n Select any oprration from the following: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n"))

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    if y>0:
        return x/y
    else:
        print("\n Divide by zero error")

if operator==1:
    a=add(num1,num2)
    print("\n Addition result is",a)
elif operator==2:
    b=sub(num1,num2)
    print("\n Subtraction result is",b)
elif operator==3:
    c=mult(num1,num2)
    print("\n Multiplication result is",c)
elif operator==4:
    d=div(num1,num2)
    print("\n Division of first number by second number results is:",d)
else:
    print("\n Invalid operator selected!")