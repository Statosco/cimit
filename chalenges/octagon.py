import turtle

getUserInput = int(input("how many sides would you like to create? "))
number = int(input("how big do you want it to be ? "))
num2 = int(input("how many number of times do you want in the second loop? "))

finalnumber = 360 / getUserInput 
for i in range(getUserInput):
    turtle.forward(number)
    turtle.right(finalnumber)
    for j in range(getUserInput):
        turtle.forward(num2)
        turtle.right(finalnumber)
turtle.done()