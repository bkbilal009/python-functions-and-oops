"""
Here is our quesiton that is give below:
 
EXTRACTION OF DIGITS 

 Q1 : Count Digit 
 Q2 : Reverse a number 
 Q3 : Check Palindrome 
 Q4 : Armstrong Number

 
"""

# Extraction of Digits

n = 48579

num = n 
while num>0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10