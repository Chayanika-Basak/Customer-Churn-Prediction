from sys import *
from scipy import *
from numpy import *
from pandas import *
from matplotlib import *
from sklearn import *
from matplotlib.pyplot import *
# print('sys {}'.format(sys.version))
# print('scipy {}'.format(scipy.__version__))
# print('numpy {}'.format(numpy.__version__))
# print('pandas {}'.format(pandas.__version__))
# print('matplotlib {}'.format(matplotlib.__version__))
# print('sklearn {}'.format(sklearn.__version__))

names = ['sepal-length','sepal-width','petal-length','petal-width','class']
ds = read_csv('/home/chayanika/Desktop/ITWorkshop/Flood_Landslide_Alert_System/ML_Basics/iris.csv', names=names)

# print(ds.shape)
# print(ds.head(13))
# print(ds.describe())
# print(ds.groupby('class').size())

ds.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
show()

