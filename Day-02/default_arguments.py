def add(num1,num2):
    num3 = num1+num2
    print(num3)

add(34,45)

def add(num1,num2=0): # You can use default value
    num3 = num1+num2
    print(num3)

add(34)

def add(num1=9,num2=0): # You can use default value
    num3 = num1+num2
    print(num3)

add()

def add(num1,num2=0): # You can use default value
    print(num1+num2)

add()