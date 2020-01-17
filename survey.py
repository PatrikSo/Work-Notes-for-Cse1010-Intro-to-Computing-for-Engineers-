denoms = [2,10,20,5,2,1]
def leastM(cash):
    bills = 0
    numBills = 0
    largestBill = 0
    for i in range(len(denoms)):
        if denoms[i] > largestBill:
            largestBill = denoms[i]
            if bills < largestBill:
                bills += largestBill
                numBills +=1
            else:
                denoms[i] = 0
    return numBills






'''''
if bills < denoms[2]:
            bills += denoms[2]
            numBills +=1
        elif bills<denoms[1]:
            bills += denoms[1]
            numBills +=1
        elif bills<denoms[3]:
            bills += denoms[3]
            numBills +=1
        elif bills<denoms[0]:
            bills += denoms[0]
            numBills +=1
        elif bills<denoms[5]:
            bills += denoms[5]
            numBills +=1
        else:
            return 0
'''''
