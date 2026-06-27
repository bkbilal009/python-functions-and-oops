a = 15 # Global varaible 

def change():
    #Local variable 
    a = 30 
    print(a)

print(a)
change()
print(a)


"""
OUtput 
15 
30 
15
"""

a = 15 # Global varaible 

def change():
    #Local variable 
    global a
    a = 30 
    print(a)

print(a)
change()
print(a)
