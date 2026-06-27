class Students: 
# Methods 

    def __init__(self): # Initializer 
       
       self.name = input("Enter your name ")
       self.age = int(input("Enter your age "))
       self.Roll_no = int(input("Enter your Roll no "))
       self.Gender = input("Enter your Gender ")


    def info(self): # You can use funciton in class but in () you can use (self) it is important...
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Roll No = {self.roll_no}")
        print(f"Address = {self.address}")
        print(f"Gender = {self.gender}")



s1 = Students
s1.info()

s2 = Students
s1.info()