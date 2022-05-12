from pandas import *
df = read_json("student.json")
df2 = read_json("student.json", orient="columns")
#orient can take columns,records,split,index,values
#json_normalize helps convert semistructured json data to pandas dataframe
print(df.head())
print(df2.head())