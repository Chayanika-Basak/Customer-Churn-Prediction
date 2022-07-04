from pandas import *
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from sklearn.linear_model import *

train_data = {'area' : [2600,3000,3200,3600,4000],
'price': [550000,565000,610000,680000,725000]}

df = DataFrame(train_data, columns=['area','price'])

print(df)
# xlabel('area(sq ft)')
# ylabel('Price(US$)')
# scatter(df.area, df.price, color='red', marker='+')
# show()


reg = LinearRegression()
print(reg.fit(df[['area']],df.price))

# price = coef*(area) + intercept (Just like y = m*x + c)
print(reg.predict([[3300]]), reg.coef_, reg.intercept_)

test_data = {'area' : [1000,1500,2300,3540,4120,4560,5490,3460,4750,2300,9000,8600,7100]}

df2 = DataFrame(test_data, columns=['area'])

res = reg.predict(df2)
ires=[]
for val in res:
    val = int(val)
    ires.append(val)
df2['prices'] = ires
print(df2)
df2.to_csv('prediction.csv', index=False)