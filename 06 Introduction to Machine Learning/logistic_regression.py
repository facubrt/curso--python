# Normalmente usada para clasificaciones binarias
# %% IRISDATASET
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=1)

x = iris.data
y = iris.target
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 20)

#print(x_test.shape)
# %% LOGISTIC REGRESSION MODEL
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
#print(logreg.predict_proba([ [5.9, 3., 5.1, 1.8] ]))
predictions_logreg = logreg.predict(x_test)
performance_logreg = metrics.accuracy_score(y_test, predictions_logreg)
print(performance_logreg)
# %%