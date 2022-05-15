import numpy as np
import pandas as pd

# create a Dataframe with 100000 rows where the data starts with 06/06/2017 00.00.00 and every
# next row is 30 secs added to the previous row
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')
df = pd.DataFrame(index=time_index)

# create a column in dataframe called 'Sale Amount' and randomly fill in values bw 1 and 10 (in dollars)
df['Sale Amount'] = np.random.randint(1,10,100000)
print(df.head(3))
print(df.shape)

#Group rows by week, calculate sum per week
print(df.resample('W').sum())

# Group by 2 weeks and calculate mean
print(df.resample('2W').mean())

#Group by month and count rows
print(df.resample('M').count())

#Group by month and count rows
print(df.resample('M', label='left').count())