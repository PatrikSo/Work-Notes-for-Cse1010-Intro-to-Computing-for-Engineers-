#1--------------------------------
#simple version
def VandSA(radius):
    volume = 4/3*3.14*radius**3
    area = 4*3.14*radius**2
    print("Volume of the radius: ",volume," Surface Area: ",area)

#non-parameter version
def VandSAinputV():
    radius = eval(input("Enter your given radius: "))
    volume = 4/3*3.14*radius**3
    area = 4*3.14*radius**2
    print("Volume of the radius: ",volume," Surface Area: ",area)
#2--------------------------------
#simple version
def pizzaPrice(diameter, price):
    radius = diameter/2
    area = 3.14*radius**2
    print( "Cost per square inch: ",price/radius,"$")

#no-parameter version
def pizzaPriceNoI():
    diameter = eval(input("Enter the diameter: "))
    price = eval(input("Enter the price: "))
    radius = diameter/2
    area = 3.14*radius**2
    print( "Cost per square inch: ",price/radius,"$")

#3--------------------------------
def molecularWeight():
    h = eval(input("Number of Hydrogen atoms: "))
    c = eval(input("Number of Carbon atoms: "))
    o = eval(input("Number of Oxygen atoms: "))
    h,c,o = h*1.008,c*12.011,o*15.999
    weight = h+c+o
    print("Moleculer weight: ",weight)

#4--------------------------------
def lightningDistance():
    seconds = eval(input("Seconds inbetween the thunder and the noise: "))
    print(seconds*1100)

#5--------------------------------
def konditoreiPrice(pounds):
    pricePerPound = pounds*10.50
    shipFee = pounds*0.86
    return pricePerPound+shipFee+1.50
#6--------------------------------
def slope():
    x1 = eval(input("Enter your x1: "))
    x2 = eval(input("Enter your x2: "))
    y1 = eval(input("Enter your y1: "))
    y2 = eval(input("Enter your y2: "))
    return (y2-y1)/(x2-x1)
#7--------------------------------
def distance():
    x1 = eval(input("Enter your x1: "))
    x2 = eval(input("Enter your x2: "))
    y1 = eval(input("Enter your y1: "))
    y2 = eval(input("Enter your y2: "))
    return (((x2-x1)**2)+((y2-y1)**2))**.5
#8--------------------------------

