#1b, Basic layout of python constructor
"""
class ...:
def __init__(self, ....):
    ....
"""

#--------------------------------------------------------------------------------------------------------------------

#2a, make a student object with multiple methods to make
class Student:
    def __init__(self, name, gpa, credits):
        self.name = name
        self.gpa = gpa
        self.credits = credits

    #getter and one setterm methods

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getGPA(self):
        return self.gpa

    def setGPA(self, newGPA):
        self.gpa = newGPA

    def getCredits(self):
        return self.credits

    def setCredits(self, newCredit):
        self.credits = newCredits

    #python toString method, printing out student info
    def __str__(self):
        return self.name + ", GPA: " + str(self.gpa) + ", CREDITS: " + str(self.credits)
    
    #b, comparing GPA's of students
    def __It__(self, otherStudent):
        return self.gpa < otherStudent.gpa

#--------------------------------------------------------------------------------------------------------------------

#3 mostly skipped (only went over how to call methods/functions), no code was given

#--------------------------------------------------------------------------------------------------------------------

#4 Researcher class inherits from Student class
class Researcher(Student):
    def __init__(self, prizes, name, gpa, credits):
        self.prizes = prizes
        Student.__init__(self, name, gpa, credits) #use the existing Student class for less code

    #adds prizes to the researcher
    def addPrizes(self, prize):
        self.prizes = self.prizes + ", " + prize

    #Researcher toString method, getting student code and simply adding new parameter "prizes" which Researcher has
    def __str__(self):
        return Student.__str__(self) + ", Prizes: " + self.prizes #again using existing Student class for less code
        
    
#------------------------------------| LAB OVER, RECURSION PRACTICE FOR CSE1725 |-------------------------------------
    
#using recursion to make a exponent method
def expo(b, n):
    #Base-case(in every recursive method, changes depending on problem)
    if n==1:
        return b
    return b * expo(b, n-1)

#using recursion to print a string backwards
def revStr(string):
    if len(string) == 0:
        return ""
    return revStr(string[1::]) + string[0]
