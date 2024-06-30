import pandas as pd
  



nFile = pd.read_excel('pile.xlxs')

#we use 2 squire brackets to select multiple table
nFile[['columsA','columnB','columnC']]

pTable = nFile.pivot_table()
print()