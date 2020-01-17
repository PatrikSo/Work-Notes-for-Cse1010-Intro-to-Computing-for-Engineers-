#lab 6
def main():
    x = eval(input("num: "))
    sum = ""
    for i in range(1,x+1):
        for j in range(1,i+1):
            sum += str(j)
        print(sum+" ")
        sum = ""

def secMain():
    n = eval(input("Enter an int: "))
    for i in range(1, n+1):
        print("")
        for j in range(1, i+1):
            print(j, end=" ")
            
def mathSearch(M, k):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == k:
                return True
    return False
    
#169 p 2,3,5

#2) C s[:len(s)-1]

#3) A ord

#4) C unicode

#171 pg 4,5


def acroo(phrase):
    seList = phrase.split()
    for i in range(len(seList)):
        print(seList[i][:1].upper(), end = ".")


def nameVal(s):
    sum = 0
    s = s.lower()
    for i in s:
        sum += ord(i) - 96
    return sum
