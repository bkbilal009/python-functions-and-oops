
# args is a argument and kwargs is a keyword arguments...
# args is a (touple) and kwargs is a (dicitonary)

def addArgs(*args):
    print(sum(args))


addArgs(34,34)
addArgs(34,54,65,76,87) 
addArgs(23)


def addArgs(*args):
    #print(sum(args))
    print(args)


addArgs([1,2],[4,5],44,900)


def addArgs(*args):
    print(args)
# shows in tuple 

addArgs(34,34)
addArgs(34,54,65,76,87) 
addArgs(23)



def add(num1,num2): 
    num3 = num1+num2
    print(num3)

add(34,34)
add(34,54,65,76,87) # shows error but you can use org in this situation 
add(23)


#++++++++++++++++++++++++++++++++ kwargs ++++++++++++++++++++++++++++++++++++++++

def addArgs(*args,**kwargs):
    #print(sum(args))
    print(kwargs)


addArgs(name = "Muhammad Bilal",age = 18 , gender = "Male")


def addArgs(*args,**kwargs):
    #print(sum(args))
    for k,v in kwargs.items():
        print(k,v)
   # print(kwargs)


addArgs(name = "Muhammad Bilal",age = 18 , gender = "Male")


def add(n1,n2,n3,*args,**kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")


add(5,10,15)


def add(n1,n2,n3,*args,**kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")


add(5,10,15,100,200,300)


def add(n1,n2,n3,*args,**kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")


add(5,10,15,100,200,300,name = "Muhammad Bilal",age=18,gender = "Male")