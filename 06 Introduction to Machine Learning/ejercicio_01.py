
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=1)

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.6, random_state = 42)

#print(iris.data)
k_values = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    performance = metrics.accuracy_score(y_test, predictions)
    k_values[k] = round(performance, 4)
    k += 1
print(k_values)

plt.plot((list(k_values.keys())), list(k_values.values()))
plt.xlabel("Values of k")
plt.ylabel = ("Performance")
plt.show()