def vicePresidents(filename):
    fileHanfle = open(filename, 'r')
    for i in fileHanfle:
        print(i, end = '')

#7
def caesar(text, key):
    str = ''
    for i in range(len(text)):
        str += chr(ord(text[i]) + key)
    return str

#9
def letterCount():
    sentence = input("Enter a sentence")
    sentence.split()
    sum = 0
    for i in range(len(sentence)):
        if sentence[i] == " " :
            sum += 0
        else:
            sum += 1
    return sum

def wordCount():
    sentence = input("Enter a sentence").split()
    return len(sentence)

#10
def wordAv():
    sentence = input("Enter a sentence").split()
    sum = 0
    for i in range(len(sentence)):
        sum += len(sentence[i])
    return sum/len(sentence)
