class Student:
    def initialize(obj, f, l, r):
        obj.fName = f
        obj.lName = l
        obj.reg = r


## main program ##
std1 = Student() # Object Instantiated
std2 = Student()

# Object initailization
# Student.initialize(std1, 'Tobi', 'Adesokan', 'MCT-UET-001')
std1.initialize('Tobi', 'Adesokan', 'MCT-UET-001')
std2.initialize('Banji', 'Egunjobi', 'MCT-UET-002')

print(std1.fName)
print(std2.reg)