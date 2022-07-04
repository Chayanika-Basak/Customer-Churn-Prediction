from sklearn import datasets

iris_dataset = datasets.load_iris()

X = iris_dataset.data[:,:2]

x_count = len(X.flat)
x_min = X[:,0].min() - 0.5
x_max = X[:,0].max() + 0.5
x_mean = X[:,0].mean()

print((x_count,x_min, x_max,x_mean,))

