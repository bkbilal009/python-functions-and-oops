def addition():

    # Scoping
    num1 = int(input("Enter first number= "))
    num2 = int(input("Enter second number= "))
    print(f"Answer = {num1 + num2}")
    
"""Scoping is the area where a variable is accessible. In python, there are four types of 
 scopes... You don't use without defining a variable. You can only use a variable after 
 defining it. 
 """ 

def subtraction():

    num1 = int(input("Enter first value = "))
    num2 = int(input("Enter second value = "))
    print(f"Answer = {num1 - num2 }")


addition()
subtraction()
