from pandas import *
df = read_csv("India_Floods_Inventory.csv")
print(df.head())
#read_excel is used to read excel files
#read_excel(url, sheetname=0, header=1)
'''
sheetname can take both the name of sheet as a string or
the index of the sheet (zero-indexed)
For multiple sheets:
sheetname=[0,1,2, "Monthly Sales"]
Returns a directory of panda dataframes containing the first, second, third
sheet and the sheet names "Monthly Sales"
'''