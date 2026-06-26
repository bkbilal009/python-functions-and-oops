# Count the number of Digits in an integer

n = 5438
num = n 
count = 0

while num > 0:
    count += 1
    num = num // 10
return count 