def Add(x, y): 
    return x + y
def Subtract(x, y):
    return x - y
def Multiply(x, y):
    return x*y
def Divide(x,y):
    return x/y

x = float(input("Input the first number here:"))
y = float(input ("Input the second number here:"))

print("What do you want to do with those numbers")
print("Select '/' for divsion")
print("Select '+' for addition")
print("Select '*' for multiplication")
print("Select '-' for subtraction")

sign = input("here:")

def switch(sign, x, y):
    if sign == '+':
        result = Add(x, y)
    elif sign == '/':
        if y == 0:
            print("You are trying to divide by 0")
        else:
            result = Divide(x, y)
    elif sign == '*':
       result= Multiply(x, y)
    elif sign == '-':
        result = Subtract(x, y)
    else:
        print("Invalid Choice")
        return
    
    print(f"Here is your result: {result}")

switch(sign, x, y)

while True:
    user_input = input("Please input enter to exit")
    if user_input:
        break