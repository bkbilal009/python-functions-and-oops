class Students:
    # Attributes || Class variable
    roll_no = 0
    name = ""
    age = 0
    gender = ""
    address = ""


# Methods

    def info(self): # You can use funciton in class but in () you can use (self) it is important...
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Roll No = {self.roll_no}")
        print(f"Address = {self.address}")
        print(f"Gender = {self.gender}")



s1 = Students() # You cann't to print the objects 
s2 = Students()
print(s1)


s1.name = "Muhammad Bilal"
s1.roll_no = 867
s1.age = 18
s1.gender = "Male"


print(s1.roll_no)
print(s1.name)
print(s1.age)
print(s1.gender)
print("++++++++++++++++++++++++++++++++")

# Print from class || bcz they have don't any value to print the function
print(s2.roll_no)
print(s2.name)
print(s2.age)
print(s2.gender)

s1.info()

print("-------------------------------------------------------------------------")

s2.info()