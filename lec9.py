def loop1_5():
    while True:
        number = float(input('Enter a positive number: '))
        if number < 0:
            break
        print(number**2)
