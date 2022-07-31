class Student:
    def __init__(self, fName, lName, reg):
        self.fName = fName
        self.lName = lName
        self.reg = reg


## main program ##
std1 = Student('Tobi', 'Adesokan', 'MCT-UET-001') # Object Instantiated and Object initailization
std2 = Student('Banji', 'Egunjobi', 'MCT-UET-002')


print(std1.fName)
print(std2.reg)