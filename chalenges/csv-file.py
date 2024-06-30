myfile = 'file.csv'


ageNumber = int(input("what age number are you trying to get, under?: "))
filenumber = int(input(f"how many people are in the under {ageNumber} list "))
namefile = []
ageFile= []


for i in range(1,filenumber + 1):
    data = input(f"\nname{i}: ")
    age = int(input(f"age{i}: "))
    namefile.append(data)
    ageFile.append(age)
    
    while age >= ageNumber:
        print(f"wow! {data} is not in under {ageNumber} list" )
        data = input(f"\nname{i}: ")
        age = int(input(f"age{i}: "))
    else:
        print(f"great! {data} is in under {ageNumber}" )
print("list writen succesfully")

with open(myfile, 'w') as file:
    for name, age in zip(namefile, ageFile):
        file.write(f"{name},{age}\n")


