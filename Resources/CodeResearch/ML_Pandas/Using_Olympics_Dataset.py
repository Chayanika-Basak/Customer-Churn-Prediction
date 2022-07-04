from numpy import *
from pandas import *

desired_width=3000
set_option('display.width', desired_width) #from pandas
set_printoptions(linewidth=desired_width) #from numpy
set_option('display.max_columns',20) #from pandas

df = read_csv("athlete_events.csv")
# print(df.head(10))
# print(df.columns)
Men = df[df['Sex']=='M']
Men = Men.dropna(subset=['Medal'])
First = Men['Name'].value_counts().index.tolist()

print(First[0])
# print(Men[Men['Name']=='Michael Fred Phelps, II'])
# print(Men['Name'].value_counts())