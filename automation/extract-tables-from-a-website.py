import pandas as pd

myList = pd.read_html('https://www.theguardian.com/football/tables')
len(myList)
print(myList[1])
