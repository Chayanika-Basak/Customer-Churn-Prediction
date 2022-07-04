from pandas import *
from numpy import *

desired_width=3000
set_option('display.width', desired_width) #from pandas
set_printoptions(linewidth=desired_width) #from numpy
set_option('display.max_columns',20) #from pandas

df = read_csv("India_Floods_Inventory.csv", na_values=[nan, 'NONE', 0])

'''SHAPE AND DESCRIBE'''
# print(df.shape)
# print(df.describe())

'''CONDITIONAL SELECTING'''
# print(df[(df['Main Cause']=='Heavy rains') & (df['Human fatality']>0) & (df['Duration(Days)']=='0') & (df['Human injured']>0)])
# print(df[df['Animal Fatality']>0])

'''REPLACING'''
# df['Main Cause'] = df['Main Cause'].replace(NaN, '0')
# df['Animal Fatality'] = df['Animal Fatality'].replace(NaN, 0)
# print(df.dtypes)
for col in df.columns:
    if(df[col].dtype==object):
        df[col] = df[col].replace(NaN,'0')
    else:
        df[col] = df[col].replace(NaN,0)
# print(df)

'''CONDITIONAL SELECTING USING SUBSTRINGS'''
# print( df[df['Main Cause'].str.contains('Flash Flood')])
# print( df[df['Main Cause'].str.contains('Landslide')])
# print( df[df['Main Cause'].str.contains('Flash Flood')]['Description of Casualties/injured'] )

'''RENAMING COLUMNS'''
# df = df.rename(columns = {"Location":"Place"})

'''MIN,MAX,MEAN,SUM,COUNT'''
# print("Maximum Human Fatality:",df['Human fatality'].max())
# print("Minimum Duration in days:",df['Duration(Days)'].min())
# print("Net Human Fatality:",df['Human fatality'].sum())
# print("Average Animal fatality:",df['Animal Fatality'].mean())
# print("Count Human Injured:",df['Human injured'].count())
# print()
# print(df.count())
#
# print()

'''CHANGING A VALUE IN DATAFRAME AND ITS DATATYPE AND APPLYING CONDITIONALS'''
# df = df.astype({'State': str})
# df['State'][544] = df['State'][544].replace('nan', 'Odisha')
# print(df[df['Human fatality'] == df['Human fatality'].max()])
# print(df.iloc[544:550])

'''UNIQUE'''
# lunique = df['Main Cause'].unique()
# for a in lunique:
#     print(a)

'''VALUE COUNTING'''
# print(df['Main Cause'].value_counts())
# print(df['Main Cause'].nunique())

'''MISSING VALUES'''
# print(df[df['Location'].isnull()])

'''DELETING COLUMNS'''
# df = df.drop('Location', axis=1)
# print(df)

'''DELETING A ROW'''
# print(df.drop([0,1], axis=0))

'''Conditionaly deleting rows'''
# print(df[~df['Main Cause'].str.contains('Heavy Rains|Heavy rains|Heavy Rain')].head(10))
# print(df[df['Main Cause'].str.contains('Heavy Rains|Heavy rains|Heavy Rain') == False].head(10))

'''DROPPING DUPLICATES'''
# print(df.drop_duplicates(subset=['Main Cause'], keep='last'))

'''GROUPBY'''
# print(df.groupby('Main Cause')['Animal Fatality'].mean())

'''Looping through df columns'''
# for col in df['Districts'][0:11]:
#     l = col.split(',')
#     print(l)

'''List Comprehension'''
# print([col.split(',') for col in df['Districts'][0:11]])

'''Applying a function over all elements'''
# print(df['Districts'].apply(lambda x: x.split(','))[0:11])

# def splitUpper(x):
#     x=x.upper()
#     return x.split(',')
#
# print(df['Districts'].apply(splitUpper)[0:11])

# df['Main Cause'] = df['Main Cause'].apply(lambda x: x.lower())
# print(df.groupby('Main Cause').apply(lambda x: x.count()))

'''Concatenating Dataframes'''
# for col in df.columns:
#      print(col, type(col), len(col))
# print(df.head(1))

# 2021 Maharashtra floods, widespread flooding in Mahad and Chiplun on 22nd July 2021 caused by exceptionally heavy rainfall
new_data = {'UEI' : 'UEI-IMD-FL-2021-0001',
       'Start Date' : '7/22/2021',
       'End Date': '7/22/2021',
       'Duration(Days)': '0',
       'Main Cause':'Heavy Rains',
       'Location': '0',
       'Districts': ' Raigad, Ratnagiri, Sindhudurg, Satara, Sangli and Kolhapur',
       'State': 'Maharashtra',
       'Latitude':0.0,
       'Longitude':0.0,
       'Severity':0.0,
       'Area Affected': 0.0,
       'Human fatality': 251,
       'Human injured': 100,
       'Human Displaced': 375000,
       'Animal Fatality': 30000,
       'Description of Casualties/injured': '''
       Due to heavy rains, more than 1,020 villages are affected in these districts. Over 375,000 people have been evacuated, 
       of whom around 206,000 are from Sangli district and around 150,000 from Kolhapur district.
       There have been more than 28,700 poultry deaths and around 300 other animal deaths in Kolhapur, 
       Sangli, Satara and Sindhudurg districts.''',
       'Extent of damage ': 'Initial estimates state that over 2 lakh (200,000) hectares of crops have been damaged in the floods',
       'Event Source': 'IMD',
       'Event Souce ID': '0'}

# print(new_data.keys())
l = list(new_data.keys())
v = list(new_data.values())
df2 = DataFrame(new_data, columns=l, index=[1027])

# df = concat([df,df2], axis=0)

'''Appending a new row'''
# row = Series(v,index=l)
# print(df.append(row, ignore_index=True))

'''Merging dataframes'''
# print(merge(df,df2,on='UEI'))
# print(merge(df,df2,on='UEI',how='outer'))
# print(merge(df,df2,on='UEI',how='left'))
# print(merge(df,df2,on='UEI',how='right'))