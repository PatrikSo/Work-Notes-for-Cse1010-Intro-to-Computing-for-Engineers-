#Q1
def isPrime(p):
    for i in range(2,p):
        if p%i == 0:
            return False
        else:
            return True

def isPrime2(p):
    rValue = True
    for i in range(2,p):
        if p%i == 0:
            rValue = False
    return rValue

#Q2
def allPrimeBelow(n):
    lst = []
    for i in range(2,n):
        if isPrime(i):
            lst.append(i)
    print(lst)

def allPrimeBelowT(n):
    lst = []
    for i in range(2,n):
        if isPrime2(i):
            lst.append(i)
    print(lst)
    return lst
#Q3
def GoldBach(n):
    if n % 2 != 0:
        return "False! Not even Goldbach"
    lst = allPrimeBelowT(n)
    for i in range(len(lst) -1, -1, -1):
        if (n - lst[i]) in lst:
            temp = str(n - lst[i]) + " + " + str(lst[i])
            return "True " + temp + " = " + str(n)
    return  "False, GoldBach is false"

#Q4
def build_file(fileName):
    fh = open(fileName, 'w')
    line = input("Enter a sentence ")
    while line != "#":
        fh.write(line + "\n")
        line = input("Enter a sentence ")
    fh.close()

#Q5
def outer(n):
    def inner(n):
        n *= 3
        print("inner: n = ",n)
        
    n += 5
    print("outer: n = ", n)
    inner(n)
    print("outer: after inner call: ",n)

