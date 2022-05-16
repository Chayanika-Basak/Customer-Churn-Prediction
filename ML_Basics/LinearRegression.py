from pandas import *
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from sklearn.linear_model import *

data = {'area' : [2600,3000,3200,3600,4000],
'price': [550000,565000,610000,680000,725000]}

df = DataFrame(data, columns=['area','price'])

print(df)
# xlabel('area(sq ft)')
# ylabel('Price(US$)')
# scatter(df.area, df.price, color='red', marker='+')
# show()


reg = LinearRegression()
print(reg.fit(df[['area']],df.price))

# price = coef*(area) + intercept (Just like y = m*x + c)
print(reg.predict([[3300]]), reg.coef_, reg.intercept_)