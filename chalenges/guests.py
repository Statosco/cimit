print("Hello!, and welcome to the party planner\n")

atending = []

noOfguest = int(input("how many guests do you want to atend to your party? "))
print("lets start building your guest list\n")
print("who are you expecting to atend?")

for i in range (1, noOfguest + 1):      
    guests = input(f"guest{i}: ")
    atending.append(guests)
    while guests.isalpha() is False:
            print("Invalid character please enter a valid name")
            guests = input(f"who are you expecting to atend: \nguest{i}: ")
    
    
print(atending)
atending.sort()
for i in atending:
    print(f"you have {i} atending")
        
qlarifie = input("will that be all? (yes or no) ").upper()

atendingGuest = atending.__len__()


if qlarifie == "YES":
    print(f"you have a list of {atendingGuest} atending guests")
    exit()
else:
    print("sure!")
    moreGuest = int(input("how many more do you want? \n"))
    for i in range (atendingGuest + 1,atendingGuest + moreGuest + 1):           
        while True:
            guests = input(f"guest{i}: ")
            if guests.isalpha():
                atending.append(guests)
                break
            else: 
                print("Iavalid character please enter a valid name")

for i in atending:
    print(f"you have {i} atending")
print(atending).upper()
                       