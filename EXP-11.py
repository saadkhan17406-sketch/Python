def add(a,b):
    sum = a+b
    print("ADDITION : ",sum)
def subtract(a,b):
    difference = a-b
    print("SUBTRACTION : ",difference)
def multiply(a,b):
    product = a*b
    print("MULTIPLICATION : ",product)
def div(a,b):
    quotient = a/b
    print("DIVISION : ",quotient)

print("*****MENU*****")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
s = int(input("SELECT THE PREFERRED OPERATION : "))
a = int(input("ENTER FIRST NUMBER : "))
b = int(input("ENTER SECOND NUMBER : "))
if s == 1 :
    add(a,b)
elif s == 2 :
    subtract(a,b)
elif s == 3 :
    multiply(a,b)
elif s == 4 :
    div(a,b)
else:
    print("INVALID CHOICE")
    exit
