import csv

namesToTRead = 'file.csv'

with open(namesToTRead, 'r') as file:
    output = csv.reader(file, delimiter= ',')
    for i in output:
        print(','.join(i))
        
