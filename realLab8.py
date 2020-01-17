import time

def readMat(fileName):
    matrix = []

    fh = open(fileName, 'r')
    # .read() returns a string
    fileContents = fh.read()
    # .split() returns a list
    fileRows = fileContents.split('\n')
    # go through fileRows
    for row in fileRows:
        # tempRow is a list of String numbers
        tempRow = row.split()
        if tempRow != ['']:
            # convert string numbers into integer
            tempRow = [int(i) for i in tempRow]
            # add tempRow(a list) into matrix(a list)
            matrix.append(tempRow)
    return matrix
    print(fileRows)
    
'''
pg 236
1) true
2) false
3) who knows
4) false
5) true
6) true (not in course)
7) false
8) false
9) true
10) false

Multiple choice
1) C
2) C
3) B
4) C(skipped)
5) B
6) C
7) A
'''
#page 238

#1
def pay(numberOfHours, hourPay):
    if numberOfHours <= 40:
        return hourPay*numberOfHours
    elif numberOfHours > 40 :
        return (40 * hourPay) + (numberOfHours - 40)*1.5*hourPay

#4
def classStanding(credit):
    if credit < 7 :
        print("Freshman")
    elif credit < 16 :
        print("Sophmore")
    elif credit < 26 :
        print("Junior")
    else:
        print("Senior")

#8
def worthy(age, citizenShip):
    if age>=30 and citizenShip >=9:
        print("Worhty of Senate")
    else:
        print("Get out")
    if age>=25 and citizenShip >=7:
        print("Worthy of Rep")
    else:
        print("Get out")

def worthy():
    age = int(input("Enter age: "))
    citizenShip = int(input("Enter years of america: "))
    if age>=25 and citizenShip >=7:
        print("Worthy of Rep")
        if age>=30 and citizenShip >=9:
            print("Worthy of Senate")
    else:
        print("Get out")
