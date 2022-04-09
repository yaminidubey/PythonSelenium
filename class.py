class Student:
    name = None
    gender = None
    age = None
    identity = None
    branch = None
    roll_number = None
    standard = 12
    subject = None
    def __init__(self,name,gender,age,identity,branch,roll_number,subject):
        self.name = name
        self.gender = gender
        self.age = age
        self.identity = identity
        self.branch = branch
        self.roll_number = roll_number
        self.subject = subject
nishank = Student('nishank','male',32,'TBE 14245','it',12377,'physics')
yamini = Student('yamini','female',25,'TBE 14334','CSE',12378,'maths')

yamini.standard = 15
print(nishank.standard)
print(yamini.standard)
print(yamini.name)
print(yamini.gender)
print(nishank.age)
