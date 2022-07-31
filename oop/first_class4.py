class Student:
    department = 'Mechatronics'
    offSubjects = ['Mech', 'LA', 'ES', 'CP-II', 'MOM', 'Proj']
    def __init__(self, fName, lName, reg):
        self.fName = fName
        self.lName = lName
        self.reg = reg
        self.email = f'{self.reg.lower()}@uet.edu.ng'
        self.courses = ['Proj']
    
    def registerSubject (self, *sub): 
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'{s} is not offered')
            if s in Student.offSubjects and s not in self.courses:
                self.courses.append(s)


## main program ##
std1 = Student('Tobi', 'Adesokan', 'MCT-UET-001') # Object Instantiated and Object initailization
std2 = Student('Banji', 'Egunjobi', 'MCT-UET-002')


std1.registerSubject('CP-II', 'MOM')
print(std1.courses)


