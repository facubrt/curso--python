#%% IRIS DATASET
import matplotlib
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

# %%
print(iris.target)

# %%
print(iris.target_names)

# %%
print(iris.data.shape)

# %%
print(iris.target.shape)

# %% IMPORTING KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# %% 
x = iris.data
y = iris.target

# %%
knn.fit(x,y)

# %%
print(knn.predict([ [5.1, 3.5, 1.4, 0.2] ]))
print(knn.predict([ [5.9, 3.,  5.1, 1.8] ]))

# %% 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.6, random_state = 42)

# %%
print(x_train.shape)
print(x_test.shape)

# %%
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
print(predictions)

# %%
from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)