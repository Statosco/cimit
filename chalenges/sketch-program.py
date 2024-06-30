import turtle

colors = ("RED, BLUE, BLACK")

print("Hello!, and welcome to drawer, what would you like to draw? ")
drawer = input(": ").upper()

print(colors)
penColor = input("which color would you like? ").upper()
while penColor not in  colors:
    print ("we dont recogonise that color today")
    input("please try a new ")
else:
    
    print(f"\nA {drawer} of {penColor} color\n")

lineLength = int(input("how long should it be? "))

angle = int(input("what angle should it be? "))


while lineLength != 0:
    turtle.color(penColor)
    turtle.forward(lineLength)
    turtle.right(360 / angle )
    lineLength = int(input("how long should it be? "))