#Lab 9

#Q1

def triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end = " ")
        print()


def whileTriangle(n):
    counter = 0
    verse = 1
    while counter != verse:
        while n != counter:
            counter += 1
            print(counter)

#Q2
def fileHandle(file):
    fh = open(file, "r")
    line = fh.readline()
    while line != "":
        print(line)
        line = fh.readLine()
    fh.close()

#Q3
def fileNumz(file):
    fh = open(file, "r")
    counter = 0
    line = fh.readline()
    while line != "":
        values = line.split(" ")
        if int(values[0] == values[1]):
            counter += 1
        line = fh.readline()
    return counter

#Q4
def lab9_notSoGood(x,y):
    while True:
        try:
            x = int(input('Enter the numerator '))
            y = int(input('Enter the denominator '))
            print('x/y= ',x/y)
            break
        except ValueError:
                print("At least one number does not seem to work")
                print("Try again")
        except ZeroDivisionError:
                print('Denominator is 0')
                print('Try again')
        except:
                print('Unknown Error')
                print('Try again')
