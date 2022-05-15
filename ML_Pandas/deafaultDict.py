from pandas import *
from numpy import *
from collections import *

df = read_csv("India_Floods_Inventory.csv")
column_names = defaultdict(str)

for name in df.columns:
    column_names[name]

print(column_names)
